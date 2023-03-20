#QR code generator using python

import qrcode as qr
import numpy

#use make() function of qrcode package to make qr code variable
#make() takes string as parameter and converts that string in qrcode and store in variable 'myinsta'
insta = qr.make("https://www.instagram.com/gupta07ayush")
Git = qr.make('https://www.github.com/gupta07ayush')
linkedin = qr.make("https://www.linkedin.com/in/gupta07ayush")

#save() function will take string as a parameter and save the qr code image naming given string.add()
insta.save("myinsta.png")
Git.save("mygit.png")
linkedin.save('mylinkedin.png')


