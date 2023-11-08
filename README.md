Shield Android RDP
This repository provides a tool for mirroring a remote Android device using a PDF payload, shield-server.jar file, and Shield.py script.

Requirements
Python 3.x
Adb (Android Debug Bridge)
Ngrok (optional, if you want to use a public URL)
Installation
Clone the repository:
Bash
git clone https://github.com/CIPHER0930/Shield-Android-RDP.git
Use code with caution. Learn more
Download and install ngrok (optional):
Bash
wget https://bin.ngrok.com/v8/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
sudo mv ngrok /usr/local/bin
Use code with caution. Learn more
Usage
Step 1: Generate a PDF payload

Connect your Android device to your computer using a USB cable.
Enable USB debugging on your Android device.
Open a terminal window and navigate to the repository directory.
Run the following command:
Bash
python Shield.py generate_pdf_payload
Use code with caution. Learn more
This will generate a PDF payload file named payload.pdf.

Step 2: Start the Shield server

Open a terminal window and navigate to the repository directory.
Run the following command:
Bash
java -jar shield-server.jar payload.pdf
Use code with caution. Learn more
This will start the Shield server, which will listen for connections from the Shield.py script.

Step 3: Start the Shield.py script

Open a terminal window and navigate to the repository directory.
Run the following command:
Bash
python Shield.py start
Use code with caution. Learn more
This will start the Shield.py script, which will connect to the Shield server and start mirroring the Android device's screen.

Step 4: Connect to the Android device

Open a web browser and navigate to the following URL:
http://<public_url>:5555
Replace <public_url> with the public URL of your ngrok tunnel, if you are using ngrok. If you are not using ngrok, use your local IP address instead.

You should now see the Android device's screen being mirrored in your web browser.

Troubleshooting
If you are having trouble connecting to the Shield server, make sure that you have started the Shield server and that your Android device is connected to the same network as your computer.

If you are having trouble mirroring the Android device's screen, make sure that you have enabled USB debugging on your Android device and that you have installed Adb.

Contributing
If you are interested in contributing to this project, please feel free to create an issue or pull request.
