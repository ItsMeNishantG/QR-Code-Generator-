# QR-Code-Generator-
Simple QR Code Generator Using Python 

A minimalist Python script that instantly converts any URL or text string into a scannable QR code image.

## Features

- **Ultra-Lightweight**: Generates a complete QR code image in just 4 lines of active Python code.
- **Instant Output**: Automatically outputs a clean, high-contrast `.png` file directly into your project directory.
- **Smartphone Readable**: Creates standard QR matrices that can be read by any modern iOS or Android camera.

## Requirements

This script uses the standard `qrcode` package for python.
- Python 3.x
- `qrcode` library
- `pillow` library (Handles the image-saving engine behind the scenes)

## Installation

Since you already have `pillow` installed on your machine, you only need to run the following command in your terminal to install the core QR module:

```bash
pip install qrcode
```

## How to Run

1. Copy the code into a file named `generate_qr.py`:

```python
import qrcode

# The data or link you want to put inside the QR code
data = "https://github.com"

# Generate the QR code image
img = qrcode.make(data)

# Save the image to your computer
img.save("github_qr.png")

print("QR Code generated successfully as 'github_qr.png'!")
```

2. Open your terminal or command prompt in the same folder and run:

```bash
python generate_qr.py
```

3. Open the newly created `github_qr.png` file in your directory and scan it with your phone!

## License

This project is open-source and available for personal use.
