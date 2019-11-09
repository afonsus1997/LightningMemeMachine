#!/usr/bin/python

import time
from escpos.printer import Usb
from PIL import Image, ImageFont, ImageDraw

WHITE = 1 
BLACK = 0

p = Usb(0x0483, 0x5720, 0)

#p.qr('LNURL1DP68GURN8GHJ7MRWW4EXCTNRDAKJ7ENPW43K2AP0VAJKUETJV96X7U30V93HGTNSDPCR76TY85ERYDNY8Y6NYCEDX3SNXDFDXSCKXWPD8P3KGVFDV4NX2C3KXGMR2DRRV9JQ28SW6J',ec=0,size=12)
p.image('craig.jpg')


#image = Image.new('1', (590,100), BLACK)

#draw = ImageDraw.Draw(image)

#draw.rectangle((0, 0, 599, 99), fill=WHITE, outline=BLACK)
#draw.text((20, 10), 'Welcome to the', fill=BLACK)
#draw.text((10, 20), 'LightningATM', fill=BLACK)
#draw.text((7, 75), '- please insert coins -', fill=BLACK)

#p.image(image)


p.cut()

#time.sleep(2)

p.cashdraw(2)
