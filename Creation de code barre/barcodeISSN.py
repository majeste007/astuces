import barcode as brc
from barcode.writer import ImageWriter
import PIL

codeB='9791075089'
barcode = brc.ISSN(codeB, writer=ImageWriter())
barcode.save('barcodeISSN')
img = PIL.Image.open('barcodeISSN.png')
img.show()