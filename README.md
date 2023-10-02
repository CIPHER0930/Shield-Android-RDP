# Shield-Android-RDP

Shield

Shield is a Python client for a remote mirroring tool called Shield. Shield allows you to mirror the screen of an Android device to your computer over the internet.

This client is easy to use and requires minimal setup. To use it, you would first need to install ngrok and Shield. Then, you would need to start the Shield server on your computer. Once the Shield server is running, you can start the Shield client on your Android device.

To start the Shield client, you would first need to set the public_url variable to the public URL that ngrok generated. Then, you would need to call the start() method.

Once the Shield client is started, it will generate a PDF payload for the current Android device. You can then click on the PDF payload to start the mirroring process.

Usage

Python
import shield

# Create a Shield client
client = shield.Shield()

# Set the public URL
client.public_url = "https://my-public-url.ngrok.io"

# Start the client
client.start()

# Wait for the user to click on the PDF payload
client.wait_for_pdf_payload_click()

# Start the mirroring process
client.start_mirroring()
Use code with caution. Learn more
Requirements

Python 3
ngrok
Shield server
License

Shield is licensed under the MIT License.
