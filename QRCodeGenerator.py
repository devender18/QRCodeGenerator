import qrcode as qr  #create alias of qrcode named 'qr' and now we don't have to write qrcode multiple time and instead of it we can use qr
from PIL import Image
# img = qr.make("https://github.com/devender18/")
# img.save("GitHub.png")

qr = qr.QRCode(version= 1, error_correction =qr.constants.ERROR_CORRECT_H,border=1)
qr.add_data("https://github.com/devender18/")
qr.make(fit=True)
img = qr.make_image(fill_color="pink",back_color="white")
img.save("newQR.png")