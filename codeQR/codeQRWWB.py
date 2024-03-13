
import qrcode
# data = "https://www.google.com"
# img = qrcode.make(data)

# img.save("google.png")

data = input("Donnez le texte ou lien de la création")
img_data = input("Donner le nom du code QR en .png ou .jpg")

code_qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
code_qr.add_data(data)
code_qr.make(fit=True)

img = code_qr.make_image(fill="black",back_color='white')
img.save(img_data)

