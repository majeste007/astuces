from barcode import Code128
import barcode as brc
from barcode.writer import ImageWriter
import PIL


codeB='PNSCOORP.'
barCode = brc.Code128(code=codeB, writer=ImageWriter())
barCode.save("pnscoorp2Code128")
img = PIL.Image.open('pnscoorp2Code128.png')
img.show()