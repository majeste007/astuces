import barcode as brc
from barcode.writer import ImageWriter
import PIL

code39 = 'NDZOKOPASCALSTEPH'
barCode = brc.Code39(code=code39, writer=ImageWriter())
barCode.save("barcodeCode39")
