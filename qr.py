import pyqrcode 
import sys
import png
from pyqrcode import QRCode
url = pyqrcode.create('http://uca.edu')
# url.svg(sys.stdout, scale=1)
# url.svg('uca.svg', scale=4)
# number = pyqrcode.create(123456789012345)
url.png('big-number.png', scale = 6)