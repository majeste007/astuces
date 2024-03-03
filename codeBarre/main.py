import barcode as brc
from barcode.writer import ImageWriter

# print(barcode.PROVIDED_BARCODES)
# help(barcode.PROVIDED_BARCODES)
code39 = 'PaSSWoRd'
barCode = brc.Code39(code=code39, writer=ImageWriter())
barCode.save("barcodeCode39t2")
print(barCode.get_fullcode())