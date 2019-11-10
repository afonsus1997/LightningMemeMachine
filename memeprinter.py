from google_images_download import google_images_download   #importing the library

from escpos.printer import Usb
from PIL import Image
import shutil
import random
import urllib
import os
import time
import sys
import signal





def meme_temeout_handler(signum, frame):
    raise Exception("end of time")

def memeprinter(keyword):
    
    #p = Usb(0x0483, 0x5720, 0)
    
    size = 580, 580
    '''
    if(len(sys.argv) == 1):
        keyword = 'bitcoin'
    else:
        keyword = sys.argv[1]    
    '''

    keyword+=' meme'
    ammount = 100
    try:
        meme_db = open(keyword + ".txt", 'r')
        urls = meme_db.readlines()
        print("[Meme Machine] - Getting memes from file\n")

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
        print("[Meme Machine] - New meme keyword, fetching meme urls\n")

    print("[Meme Machine] - Choosing a meme..." + "\n")

    signal.signal(signal.SIGALRM, meme_temeout_handler)
    signal.alarm(6)
    

    try:
        while(True):
            linenumber = random.randint(0,ammount-1)
            memeurl = urls[linenumber] 
            extension = os.path.splitext(memeurl[:-1])[1]
            #print(extension)
            if(extension == ".bmp" or extension == ".jpg" or extension == ".jpeg" or extension == ".png" ):
                break

        succeed=True
        while True:
            try:
                urllib.request.urlretrieve(memeurl[:-1], "meme." + extension)        
                #succeed = True
            except:
                succeed = False
                linenumber = random.randint(0,ammount-1)
                memeurl = urls[linenumber] 
                extension = os.path.splitext(memeurl[:-1])[1]
            if succeed:
                break


        print("[Meme Machine] - Chosen meme: " + memeurl + "\n")


        time.sleep(1)

        print("[Meme Machine] - Resizing meme..." + "\n")


        basewidth = 580
        img = Image.open("meme."+ extension)
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)

        #img.show()
        img.save("meme." + extension) 

        print("[Meme Machine] - Printing meme..." + "\n")




        p.image("meme." + extension)
        p.cut()

        print("[Meme Machine] - Cleaning session..." + "\n")


        if os.path.exists("meme." + extension):
            os.remove("meme." + extension)
        else:
            print("[Meme Machine] - Nothing to clean" + "\n")

        print("[Meme Machine] - Everything done!" + "\n")

        return 1

    except Exception:
        print("[Meme Machine] - Meme temeout exceeded!\n")

        return -1



#memeprinter("bitcoin")











