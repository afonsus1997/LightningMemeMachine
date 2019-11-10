#!/usr/bin/python3

import time
from escpos.printer import Usb
from PIL import Image, ImageDraw, ImageFont
import os

import plotly.graph_objects as go
import pandas as pd

#import urllib.request

#response = urllib.request.urlopen('http://www.cryptodatadownload.com/cdd/Kraken_BTCUSD_1h.csv')
#csvfile = response.read


def printchart():

      df = pd.read_csv('http://www.cryptodatadownload.com/cdd/gemini_BTCUSD_1hr.csv', skiprows=1)
      df=df.head(50)


      fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                  open=df['Open'], high=df['High'],
                  low=df['Low'], close=df['Close'])
                        ])


      fig.update_layout(xaxis_rangeslider_visible=False, width=580, height=400)

      fig.write_image("fig1.png")
      #fig.show()




      WHITE = 1 
      BLACK = 0

      p = Usb(0x0483, 0x5720, 0)
      recipt = Image.new('1', (580,500), 1)



      x1 = 0
      y1 = 0

      im2 = Image.open('btclogo.png')
      recipt.paste(im2)


      x1 = 0
      y1 = 149

      im1 = Image.open('fig1.png')
      recipt.paste(im1, (x1, y1))



      #draw = ImageDraw.Draw(recipt)

      #UbuntuFont = ImageFont.truetype("fonts/Ubuntu-MediumItalic.ttf")

      #msg='Bitcoin Chart BTCUSD'
      #draw.text((0, 410), msg, fill=BLACK, font=UbuntuFont)

      #LOCAL SAVE
      #recipt.save("tmp.png")
      #os.system("open tmp.png")

      p.image(recipt)


      #p.image('fig1.png', high_density_vertical=True, high_density_horizontal=True, impl=u'bitImageRaster', fragment_height=960)


      p.cut()

      '''

      p.qr('LNURL1DP68GURN8GHJ7MRWW4EXCTNRDAKJ7ENPW43K2AP0VAJKUETJV96X7U30V93HGTNSDPCR76TY85ERYDNY8Y6NYCEDX3SNXDFDXSCKXWPD8P3KGVFDV4NX2C3KXGMR2DRRV9JQ28SW6J',ec=0,size=12)
      p.image('craig.jpg')




      p.cut()

      time.sleep(2)

      p.cashdraw(2)

      '''
