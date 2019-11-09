from google_images_download import google_images_download   #importing the library

from escpos.printer import Usb
from PIL import Image
import shutil
import random
import urllib
import os
import time
import sys



p = Usb(0x0483, 0x5720, 0)


size = 580, 580
if(len(sys.argv) == 1):
    keyword = 'bitcoin'
else:
    keyword = sys.argv[1]    


keyword+=' meme'
ammount = 100
try:
    meme_db = open(keyword + ".txt", 'r')
    urls = meme_db.readlines()
    print(urls)

except:
    meme_db = open(keyword + ".txt", 'w')
    search = {"keywords":keyword,"limit":ammount,"print_urls":False, "no_download":True, "safe_search":True}
    response = google_images_download.googleimagesdownload()   #class instantiation
    paths = response.download(search)
    for i in range(ammount):
        meme_db.write(paths[0].get(keyword)[i] + '\n')
    meme_db.close()
    meme_db = open(keyword + ".txt", 'r')
    urls = meme_db.readlines()


linenumber = random.randint(0,ammount-1)
print(linenumber)
memeurl = urls[linenumber] 
print("\n\n" + memeurl + "\n\n")

succeed=True
while True:
    try:
        urllib.request.urlretrieve(memeurl[:-1], "meme.jpg")
    except:
        succeed = False
        linenumber = random.randint(0,ammount-1)
        print(linenumber)
        memeurl = urls[linenumber] 
        print("\n\n" + memeurl + "\n\n")
    if succeed:
        break


print("\n\nresizing...\n\n")

time.sleep(1)

basewidth = 580
img = Image.open("meme.jpg")
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)

img.show()
img.save("meme.jpg") 

print("\n\nDone!\n\n")

'''
for i in range(ammount):
    path=paths[0].get(keyword)[i]
    print(path)
    p.image(path)
    p.cut()
'''
print("\n\nCrearing session!\n\n")

#p.image("meme.jpg")
#p.cut()

if os.path.exists("meme.jpg"):
  os.remove("meme.jpg")
else:
  print("The file does not exist")