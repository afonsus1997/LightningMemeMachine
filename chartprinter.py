#!/usr/bin/python

import time
from escpos.printer import Usb
from PIL import Image, ImageFont, ImageDraw

import plotly.graph_objects as go
import pandas as pd

#import urllib.request

#response = urllib.request.urlopen('http://www.cryptodatadownload.com/cdd/Kraken_BTCUSD_1h.csv')
#csvfile = response.read



df = pd.read_csv('http://www.cryptodatadownload.com/cdd/Kraken_BTCUSD_1h.csv', skiprows=1)
df=df.head(50)


fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'], high=df['High'],
                low=df['Low'], close=df['Close'])
                      ])


fig.update_layout(xaxis_rangeslider_visible=False, width=800, height=400)

fig.write_image("fig1.png")
#fig.show()




WHITE = 1 
BLACK = 0

p = Usb(0x0483, 0x5720, 0)
image = Image.new('1', (800,800), 1)

x1 = 0
y1 = 420

im1 = Image.open('fig1.png')
image.paste(im1, (x1, y1, x1 + 800, y1 + 400))


x1 = 0
y1 = 0

im1 = Image.open('btclogo.png')
image.paste(im1, (x1, y1, x1 + 800, y1 + 400))

#draw = ImageDraw.Draw(image)
#draw.rectangle((0, 0, 599, 99), fill=WHITE, outline=BLACK)

msg='Bitcoin Chart BTCUSD'
w, h = draw.textsize(msg)
draw.text(((800-w)/2, 410), msg, fill=BLACK)




p.image(image)


#p.image('fig1.png', high_density_vertical=True, high_density_horizontal=True, impl=u'bitImageRaster', fragment_height=960)


p.cut()

'''

p.qr('LNURL1DP68GURN8GHJ7MRWW4EXCTNRDAKJ7ENPW43K2AP0VAJKUETJV96X7U30V93HGTNSDPCR76TY85ERYDNY8Y6NYCEDX3SNXDFDXSCKXWPD8P3KGVFDV4NX2C3KXGMR2DRRV9JQ28SW6J',ec=0,size=12)
p.image('craig.jpg')




p.cut()

time.sleep(2)

p.cashdraw(2)

'''
