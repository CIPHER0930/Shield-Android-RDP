import ngrok
import socket
import struct
import time
from time import sleep
from typing import Any, Callable, Optional, Tuple, Union

import numpy as np
import numpy.typing as npt

from adbutils import AdbDevice, AdbError, Network, _AdbStreamConnection, adb
from av.codec import CodecContext

from .const import EVENT_FRAME, EVENT_INIT, LOCK_SCREEN_ORIENTATION_UNLOCKED
from .control import ControlSender

Frame = npt.NDArray[np.int8]

VERSION = "1.20"
HERE = Path(file).resolve().parent
JAR = HERE / "shield-server.jar"


class Shield(Client):
  """
  Create a shield client.
  This client won't be started until you call .start()

  Args:
    kwargs: Any argument that is supported by the parent class.
  """

  def init(self, pdf_payload: bytes, **kwargs):
    super().init(**kwargs)

    try:
      # Start ngrok and get the public URL
      ngrok.connect(port=5555)
      self.public_url = ngrok.get_public_url()
    except (ConnectionRefusedError, ngrok.CommandFailedError) as e:
      # If ngrok is not running or encounters an error, raise an exception
      raise Exception(f"Failed to start ngrok: {e}")

    # Set the PDF payload
    self.pdf_payload = pdf_payload

  def __init_server_connection(self) -> None:
    """
    Connect to the Android server, there will be two sockets: video and control sockets.
    This method will also set the resolution property.
    """

    # Upload the PDF payload to a web server
    try:
      self._upload_pdf_payload()
    except Exception as e:
      # If there is an error uploading the PDF payload, raise an exception
      raise Exception(f"Failed to upload PDF payload: {e}")

    # Connect to the Shield server using the PDF payload
    try:
      self.__video_socket = socket.create_connection((self.public_url, 5555))
      self.control_socket = socket.create_connection((self.public_url, 5555))
    except (ConnectionRefusedError, socket.timeout) as e:
      # If the Shield server is not running or connection fails, raise an exception
      raise Exception(f"Failed to connect to Shield server: {e}")

    self.device_name = self.__video_socket.recv(64).decode("utf-8").rstrip("\x00")
    if not len(self.device_name):
      raise ConnectionError("Did not receive Device Name!")

    # Get the resolution from the Android device
    try:
      resolution = self.adb_device.get_prop("ro.product.width_height")
    except AdbError as e:
      raise Exception(f"Failed to get resolution from Android device: {e}")

    width, height = [int(x) for x in resolution.split("x")]
    self.resolution = (width, height)

  def _generate_pdf_payload(self) -> bytes:
    """
    Generate a PDF payload for the current Android device.

    Returns:
      A bytes object containing the PDF payload.
    """

    # Generate a PDF payload using pdftk
    # Create a temporary file to store the PDF payload
    with tempfile.NamedTemporaryFile(suffix=".pdf") as temp_file:

      # Generate a PDF payload with pdftk
      try:
        subprocess.run(["pdftk", "--dump-data", temp_file.name], input=self.device_name.encode("utf-8"))
      except (subprocess.CalledProcessError, FileNotFoundError) as e:
        # If there is an error generating the PDF payload, raise an exception
        raise Exception(f"Failed to generate PDF payload: {e}")

      # Read the PDF payload from the temporary file
      with open(temp_file.name, "rb") as f:
        pdf_payload = f.read()

      # Return the PDF payload
      return pdf_payload

  def on_pdf_payload_clicked(self):
    """
    This method will be called when the PDF payload is clicked
    def on_pdf_payload_clicked(self):
    # Get the URL of the PDF payload
    url = self.pdf_payload.decode("utf-8")

    # Open a web browser to the URL of the PDF payload
    web_browser = webbrowser.get(self.device_name)
    web_browser.open(url)

