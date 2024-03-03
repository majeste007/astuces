import barcode
from barcode.writer import ImageWriter
import PIL

# creating Bar Code in using ISBN13 
#  ISBN must start with 97910 or 97911.
num = '979107508719'
bar_code = barcode.ISBN13(num,writer=ImageWriter())
bar_code.save('barcodeISBN13')
img= PIL.Image.open('barcodeISBN13.png')
img.show()
