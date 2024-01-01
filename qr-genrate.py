"""
Generate a customized QR code with an artistic background.

Required libraries:
- segno: For creating QR codes (https://segno.readthedocs.io/en/stable/index.html)
- pillow: For image processing
- qrcode-artistic: For artistic QR code features

Installation:
    pip install segno pillow qrcode-artistic

User needs Python 3.7 or newer to run this code.
"""

import segno
from enum import Enum

# Define colors using an Enum for clarity and reusability
class Color(Enum):
    INF_GREEN = "#01c796"  # Infrrd green
    BLACK = "#000000"
    WHITE = "#ffffff"

# Message to be encoded in the QR code
message = "Happy New Year 2024, Infrrd!"

# Filename for the generated QR code image
file_name = "hny-2024.png"

# Create a QR code instance using segno
qrcode = segno.make_qr(message)

# Apply artistic customizations:
qrcode.to_artistic(
    background="inf_logo.jpeg",  # Use Infrrd logo as background
    target=file_name,  # Save the QR code to the specified file
    scale=10,  # Adjust QR code size
    dark=Color.INF_GREEN.value,  # Set primary color to Infrrd green
    quiet_zone=Color.WHITE.value,  # Set quiet zone color to white
    finder_dark=Color.BLACK.value,  # Set finder patterns to black
    data_dark=Color.INF_GREEN.value,  # Set data modules to Infrrd green
    border=2,  # Add a 2-pixel border for visual clarity
)
