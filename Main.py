import qrcode

# The data or link you want to put inside the QR code
data = "https://github.com"

# Generate the QR code image
img = qrcode.make(data)

# Save the image to your computer
img.save("github_qr.png")

print("QR Code generated successfully as 'github_qr.png'!")
