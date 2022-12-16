from barcode import EAN13
from barcode.writer import ImageWriter

with open(r'C:\Users\Rafael Campos\Downloads\barcode.png', 'wb') as f:
    EAN13('01234567899876543210', writer=ImageWriter()).write(f)
