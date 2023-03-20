# python program to make advanced QR code generator 
# we will design color and border of the QR code.
# install qrcode package using pip
# install pillow library using pip

import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=4,)

qr.add_data("https://www.youtube.com/@gupta07ayush/")
qr.make(fit=True)

img = qr.make_image(fill_color='green',
                    back_color="aqua")

img.save("ayushyoutube.png")