# QR Code Generator

This repository contains a Python script to generate a customized QR code with an artistic background, embedding a New Year's greeting.

## Requirements

- Python 3.7 or newer
- Required libraries:
    - segno ([https://segno.readthedocs.io/en/stable/index.html](https://segno.readthedocs.io/en/stable/index.html))
    - pillow
    - qrcode-artistic

## Installation

1. Clone this repository:

   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/happy-new-year-qr-code.git
   ```
2. Install the required libraries:
    ```bash
    pip install segno pillow qrcode-artistic
    ```

## Usage
1. Navigate to the project directory:
    ```bash
    cd qrcode-generator
    ```
2. Run the Python script:
    ```bash
    python qr-genrate.py
    ```
3. This will create a QR code image named "hny-2024.png" in the same directory.

## Customization

You can modify the message variable in the script to change the embedded text.
Experiment with different colors and background images to create your own unique QR code designs.

## Scanning the QR Code

Use a QR code scanner app, such as Google Lens, to scan the generated QR code.
The app will display the embedded message "Happy New Year 2024, Infrrd!"

## Additional Notes

The inf_logo.jpeg file is used as the background image in the script. Ensure it's present in the same directory as the Python script.
For more details on customizing QR codes with segno, refer to the official documentation: https://segno.readthedocs.io/en/stable/index.html
