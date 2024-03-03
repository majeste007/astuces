
import barcode as brc
from barcode.writer import ImageWriter
import PIL


codeB='9791075089'
barCode = brc.ISBN10(codeB, writer=ImageWriter())
barCode.save("brcodeISBN10")
img = PIL.Image.open('brcodeISBN10.png')
img.show()