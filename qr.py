import pyqrcode 
import sys
import png
from pyqrcode import QRCode
url = pyqrcode.create('https://linktr.ee/minhhoang176')
# url.svg(sys.stdout, scale=1)
# url.svg('uca.svg', scale=4)
# number = pyqrcode.create(123456789012345)
url.png('profile.png', scale = 6)