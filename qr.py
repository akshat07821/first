import qrcode

data = r"C:\Users\AKSHAT DUBEY\OneDrive\Desktop\html\2.1 Heading Element\first.html"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save("qrcode.png")

img.show()