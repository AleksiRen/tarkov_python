try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pyautogui
import pyscreenshot as ImageGrab
import os
import time
import cv2
import numpy as np
import platform
import subprocess
import random
import sys
import keyboard
import asyncio
import os
from playsound import playsound

# os.system("taskkill /im dialog /f")
# import playsound
from playsound import playsound

# import winsound
# winsound.PlaySound("ding.wav", winsound.SND_ASYNC)


print(pyautogui.position())
is_retina = False
if platform.system() == "Darwin":
    is_retina = subprocess.call("system_profiler SPDisplaysDataType | grep 'retina'", shell=True)


def imagesearch_loop1(image, timesample, precision=0.8):
    pos = imagesearch(image, precision)
    while pos[0] == -1:
        print(image + " not found, waiting")
        time.sleep(timesample)
        pos = imagesearch(image, precision)
    return pos


def region_grabber(region):
    if is_retina: region = [n * 2 for n in region]
    x1 = region[0]
    y1 = region[1]
    width = region[2] - x1
    height = region[3] - y1

    return pyautogui.screenshot(region=(x1, y1, width, height))


def imagesearchareaT(image, x1, y1, x2, y2, precision=0.8, im=None):
    if im is None:
        im = region_grabber(region=(x1, y1, x2, y2))
        if is_retina:
            im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
        # im.save('testarea.png') usefull for debugging purposes, this will save the captured region as "testarea.png"

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return False

    return True


def imagesearcharea(image, x1, y1, x2, y2, precision=0.8, im=None):
    if im is None:
        im = region_grabber(region=(x1, y1, x2, y2))
        if is_retina:
            im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
        # im.save('testarea.png') usefull for debugging purposes, this will save the captured region as "testarea.png"
        im.save('testarea.png')

    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc


def imagesearch_loop(image, timesample, x1, y1, x2, y2, precision=0.8, im=None, ):
    pos = imagesearcharea(image, x1, y1, x2, y2, precision=0.8, im=None)
    while pos[0] == -1:
        print(image + " not found, waiting")
        time.sleep(timesample)
        pos = imagesearch(image, precision)
    return True


async def alle50():
    try:
        im1 = ImageGrab.grab(bbox=(1260, 160, 1368, 188))
        im1.save('im1.png')
        x = pytesseract.image_to_string(Image.open('im1.png'))
        x = x.replace(" ", "")
        y = int(x)
        await asyncio.sleep
        if y >= 50000:
            playsound('ding2.mp3')



    except ValueError:
        print("Ei tunnista.")


def click_image(image, pos, action, timestamp=1, offset=5):
    img = cv2.imread(image)
    height, width, channels = img.shape
    pyautogui.moveTo(pos[0] + random(width / 2, offset), pos[1] + random(height / 2, offset),
                     timestamp)
    pyautogui.click(button=action)


def imagesearch(image, precision=0.8):
    im = pyautogui.screenshot()
    if is_retina:
        im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
    # im.save('testarea.png') useful for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc




def vaaka():
    # FAL ase pystykuva koordinaatit ensimmainen
    x1 = 1254
    x2 = 1399
    y1 = 74
    y2 = 455
    # lippaan kuvan etsinnan koordinaatit
    x3 = 730
    x4 = 952
    y3 = 713
    y4 = 923
    # toisen lippaan etsimisen koordit
    xx3 = 1299
    xx4 = 1566
    yy3 = 725
    yy4 = 926
    lipasC = [847, 370, 1161, 558]

    # ekan lippaan dragauskoordinaatit
    x5 = 1545
    y5 = 650
    # scrolli
    scrol = 0
    # %5 resetin jlk draggayskoordinaatit lippaasta aseeseen
    # uusi aseen koordinaatti lippaan draggaykseen
    ylip = 0
    # vaaka arvot falikuvan etsimiselle
    ax = 1264
    ay = 80
    ax2 = 1641
    ay2 = 205

    pyautogui.click(x=1660, y=552)
    for i in range(1, 35):
        pyautogui.scroll(1)
    pyautogui.moveTo(x=1899, y=406)
    pyautogui.dragTo(1887, 692, 2, button='left')



    for i in range(0, 26):
        print("kierros",i)
        print("ax=",ax,"ax2= ",ax2, "ay=", ay, "ay2= ",ay2)
        if i%2==0  and i != 0:
            # x akseli resetti
            ax = 1264
            ax2 = 1641
            ay +=126
            ay2 +=126

        if i == 12:
            pyautogui.click(x=1660, y=552)
            for i in range(1, 14):
                pyautogui.scroll(-1)

            ax = 1264
            ax2 = 1641
            ay =179
            ay2 =305

        falkuva = imagesearcharea("falkuva1.png", x1, y1, x2, y2, precision=0.7, im=None)


        falkuva1 = imagesearcharea("falkuva.png", ax, ay, ax2, ay2, precision=0.7, im=None)
        falextreme = imagesearcharea("falextremeV.png", ax, ay, ax2, ay2, precision=0.7, im=None)
        falEL = imagesearcharea("lyhytfalV.png", ax, ay, ax2, ay2, precision=0.7, im=None)
       # kivaa = ImageGrab.grab(bbox=(ax, ay, ax2, ay2))
        #kivaa.show()


        # PYSTYASENTOETSINTA


        # VAAKATASOSEARcHI
        if falkuva1 != [-1, -1] or falextreme != [-1, -1] or falEL != [-1, -1]:

            pyautogui.click(ax + falkuva1[0] + 20, ay + falkuva1[1] + 20, button='right')
            time.sleep(0.2)
            #etsii klikatun inspectí ikkunan
            ins = (imagesearch("inspect.png", precision=0.5))
            print("inspectikuva: ", ins)
            time.sleep(0.2)
            #klikkaa inspectiä
            pyautogui.click(ins[0] + 2, ins[1] + 5)
            time.sleep(0.3)
            #etsii lipasta inspectistä
            lipas = imagesearcharea("lipas.png", x3, y3, x4, y4)

            print(lipas)

            #jos lipasta ei löydy, siirrytaan seuraavaan aseeseen
            if lipas[0] == -1:
                ax += 250
                ax2 += 253

                pyautogui.press('esc')
                #JOS TARVII DRAGATA LIPAS POIS
            if lipas[0] != -1:
            #     #jos ase on extreme, annetaan eri koordinaatit, jotta draggays onnistuu
            #     if falextreme == [-1, -1]:
            #
            #         pyautogui.moveTo(990, 70)
            #         pyautogui.dragTo(1722, 78, 2)
            #     else:
            #         pyautogui.moveTo(985, 8)
            #         pyautogui.dragTo(1722, 78, 2)

                lipas = imagesearcharea("lipas.png", x3, y3, x4, y4)
                # lippaan päälle hiiri
                pyautogui.moveTo(x3 + lipas[0] + 3, y3 + lipas[1] + 3, 0.5)
                #VANHA LIPPAAN ETSIMISBOKSI JOS DRAGGAA INSPECTI RUUDUN OIKEAAN REUNAAN
                #pyautogui.moveTo(xx3 + lipas[0] + 3, yy3 + lipas[1] + 3, 0.5)
                pyautogui.keyDown('ctrl')
                pyautogui.click()
                pyautogui.keyUp('ctrl')
                # vetaa lippaan reppuun
                #--vanha
                # pyautogui.dragTo(1128, 631, 1.5)
                #--vanha
                # pyautogui.click(1128, 631, button='right')
                #--uusi ctrl
                pyautogui.press('esc')
               # pyautogui.click(879, 507, button='right')
                # klikkaa unload ammo'
               # time.sleep(0.2)

                #--vanha drag
                # pyautogui.click(1128 + 20, 631 - 82)
                #--uus ctrl
                #time.sleep(0.3)
               # pyautogui.click(889, 416)
                #  time.sleep(1.5)

                #--vanha drag
               # pyautogui.moveTo(1128, 631, 0.4)
                #--uus ctrl
               # pyautogui.moveTo(879, 507, 0.4)
                lipasreppu = imagesearcharea("lipasiso3.png", lipasC[0], lipasC[1], lipasC[2], lipasC[3], precision=0.5)
                if lipasreppu != [-1, -1]:
                    pyautogui.moveTo(lipasC[0] + lipasreppu[0] + 5, lipasC[1] + lipasreppu[1] + 5)
                    pyautogui.click(button='right')
                    pyautogui.click(lipasC[0] + lipasreppu[0] + 50, lipasC[1] + lipasreppu[1] - 88)
                    pyautogui.moveTo(lipasC[0] + lipasreppu[0] + 5, lipasC[1] + lipasreppu[1] + 5)
                    pyautogui.dragTo(ax + 40, ay + 60 + ylip, 1.5)


                ax += 250
                ax2 += 253
                x5 + 51


        else:
            ax += 250
            ax2 += 253

#vaaka()
def ammukset():
    #ammojen etsinnän boksi oikee ala

    x3=1161
    y3=632


    #ammokuvan boksi
    x1 = 910
    x2 = 973
    y1 = 441
    y2 = 506
    #tesseract
    x4 = 892
    y4 = 487
    x5 = 910
    y5 = 506
    #ammo coordiarray
    ammocoord=[]
    #lista, jonka mukaan jätetään jo kokeiltuja ammokasojen yhdistämisiä tekemättä
    ammocoord2=[]

    ammoboxcoord=[]
    #koordinaatit kierroksen vedettävään ammokasaan
    xxx = 0
    yyy = 0
    #ensimmäinen ja toinen indeksi listassa oleville koordinaateille
    kr1 = 0
    kr2 = 1
    #sen hetkisen kierroksen ammokasa, joka on vedettävänä
    xxxx =0
    yyyy=0
    kr3 = 0
    kr4= 1
    #ammoboxcoordi
    t= 0
    tt=0
    ttt=0
    tttt=0

    kr5=0
    kr6=1
    kr7=2
    kr8=3


    for i in range(1, 14):
        print(i%5)

        if i % 5 == 0 and i != 10 or i == 9:
            y1+=63
            y2+=63
            x1 = 910
            x2 = 973

        ammo = imagesearcharea('ammo.png', x1, y1, x2, y2)
       # kivaa = ImageGrab.grab(bbox=(x1, y1, x2, y2))
       # kivaa.show()
        print(ammo)
        if ammo != [-1, -1]:

            pyautogui.moveTo(x1+3,y1+3)
            time.sleep(0.2)
            #antaa kuvan ylävasen koordinaatit jokaiselle ammuskasalle
            ammocoord += x1 + 3, y1 + 3
            ammocoord2 += x1 + 3, y1 + 3
            #jokaisen ammuskasan imagesearch boxi koordinaatit
            ammoboxcoord += x1,y1,x2,y2

            x1 += 63
            x2 += 63
            x4 += 63
            x5 += 63
        else:
            break


    ammopituus = len(ammocoord)
    kierrosmaara = ammopituus // 2
    kierrosmaara2 = ammopituus // 2
    nytpituus=kierrosmaara
    nytpituus2=kierrosmaara
    print("ammcoordilista: ",ammocoord)

    print("ammopituus/2: ", ammopituus//2)

    for i in range(0, kierrosmaara):
        print("ylempi pituus", nytpituus)
        kr3 = 0
        kr4 = 1
        # dragattava
        xxx = ammocoord[kr1]
        yyy = ammocoord[kr2]
        print("kierrokset: ", ammopituus//2 )

        for i in range(0, kierrosmaara2):

            print("alempi pituus",nytpituus2)
            # kohde
            xxxx = ammocoord2[kr3]
            yyyy = ammocoord2[kr4]
            t = ammoboxcoord[kr5]
            tt = ammoboxcoord[kr6]
            ttt = ammoboxcoord[kr7]
            tttt = ammoboxcoord[kr8]

            # jos dragattava on itsensa kohde
            if xxxx == xxx and yyyy==yyy:
                kr3 += 2
                kr4 += 2

                print("skippaa taman",i)

            else:
                print("tama onnistuu", i)

                # dragattavan paalle hiiri
                pyautogui.moveTo(xxx, yyy)
                # draggaa dragattavaan
                pyautogui.dragTo(xxxx+20, yyyy+25, 1)
                #katsoo onko paikka tyhjentynyt
                ammo2 = imagesearcharea('ammo.png', t, tt, ttt, tttt)
                ammo3 = imagesearcharea('ammo2.png', t, tt, ttt, tttt)

              #  print("ammonhaku kuva koordit:",ammo2)
               # kivaa = ImageGrab.grab(bbox=(t, tt, ttt, tttt))
               # kivaa.show()

                if ammo2 == [-1,-1] and ammo3 == [-1,-1]:
                     del ammocoord[kr1]
                     del ammocoord[kr1]
                     #del ammocoord2[kr1]
                     #del ammocoord2[kr1]

                     kr1-=2
                     kr2-=2
                     kr3-=2
                     kr4-=2
                     kierrosmaara -=1
                     nytpituus2 -= 1


                     break


                # seuraava dragattava
                kr3 += 2
                kr4 += 2
                nytpituus2 -= 1

        print("toisen ammon kaikki", ammocoord2)
        print("poistaa ", kr1, ":n indeksin listalta")
        del ammocoord2[0]
        del ammocoord2[0]
        print("montaks: ", ammocoord2)
        kierrosmaara2-=1

        kr1 += 2
        kr2 += 2
        # lisää arvjoja seuraavaa boksi koordinaattisettiä varten
        kr5 += 4
        kr6 += 4
        kr7 += 4
        kr8 += 4
        nytpituus -= 1

    #print("nain monta jaljella",len(ammocoord))
    if len(ammocoord) >0:

        #indeksit listan ekoille arvoille
        u1= 0
        u2=1
        for i in range(0,len(ammocoord)//2):
            print("monesko:",i)


            pyautogui.moveTo(ammocoord[u1],ammocoord[u2])
            pyautogui.dragTo(pyautogui.dragTo(942, 725,1))
            u1+=2
            u2+=2

def falmyynti2():
    #FAL ase pystykuva koordinaatit ensimmainen
    x1=1254
    x2=1399
    y1=74
    y2=455
    #lippaan kuvan etsinnan koordinaatit
    x3=730
    x4= 952
    y3=713
    y4=923
    #toisen lippaan etsimisen koordit
    xx3=1299
    xx4= 1566
    yy3=725
    yy4= 926
    #lippaan etsintäkooordit repussa
    lipasC=[847, 370, 1161, 558]

    #ekan lippaan dragauskoordinaatit
    x5=1545
    y5=650
    #scrolli
    scrol = 3
    #%5 resetin jlk draggayskoordinaatit lippaasta aseeseen
    #uusi aseen koordinaatti lippaan draggaykseen
    ylip = 0
    #vaaka arvot falikuvan etsimiselle
    ax= 1264
    ay= 80
    ax2= 1641
    ay2= 205

   # pyautogui.click(x=1660, y=552)
    #jos haluaa klikata sivun ylös, spammii joku 4 kertaa
    pyautogui.click(1901, 93, 2)




    pyautogui.click(x=1660, y=552)
    for i in range(1,35):
        pyautogui.scroll(1)
    pyautogui.moveTo(x=1899, y=406)
    pyautogui.dragTo(1887, 716, 2, button='left')
    print("moi")


    for i in range(0,20):
        print(i,"kierrokset vilisee silimissä")
        if i ==5:
            pyautogui.click(x=1660, y=552)
            for i in range(1, scrol+4):
                pyautogui.scroll(-1)
            # x akseli resetti
            x1 = 1254
            x2 = 1399
            scrol += 6
            #ylip += 375
        if i == 10:
            pyautogui.moveTo(x=1660, y=552)
            #pyautogui.click(x=1568, y=18)
            for i in range(1, 10):
                pyautogui.scroll(-1)
            x1 = 1264
            x2 = 1389
            y1= 179
            y2= 557
        if i == 15:
            x1 = 1264
            x2 = 1389
            y1= 556
            y2 = 934

        falkuva =imagesearcharea("falkuva1.png", x1, y1, x2, y2, precision=0.7, im=None)
        falkuvaextP =imagesearcharea("falextremepysty.png", x1, y1, x2, y2, precision=0.7, im=None)
        falkuvaextLP =imagesearcharea("lyhytfalP.png", x1, y1, x2, y2, precision=0.7, im=None)
        print(falkuva, falkuvaextLP, falkuvaextP)
       # kivaa = ImageGrab.grab(bbox=(x1, y1, x2, y2))
       # kivaa.show()

        #PYSTYASENTOETSINTA
        if falkuva !=[-1,-1] or falkuvaextP != [-1,-1]or falkuvaextLP != [-1,-1]:
            print("normifal:", falkuva, " extreme:",falkuvaextP)
            pyautogui.click(x1+falkuva[0]+20,y1+falkuva[1]+20, button='right')
            time.sleep(0.2)
            ins = (imagesearch("inspect.png", precision=0.5))
            print("inspectikuva: ",ins)
            time.sleep(0.2)

            pyautogui.click(ins[0] + 2, ins[1] + 5)
            time.sleep(0.3)
            lipas= imagesearcharea("lipas.png",x3, y3, x4, y4)



            print(lipas)


            if lipas[0]== -1:
                x1 += 127
                x2 += 127

                pyautogui.press('esc')
            if lipas[0] != -1:

                #lipas
               #lipas = imagesearcharea("lipas.png", x3, y3, x4, y4)
                # lippaan päälle hiiri
                pyautogui.moveTo(x3 + lipas[0] + 3, y3 + lipas[1] + 3, 0.5)
                pyautogui.keyDown('ctrl')
                pyautogui.click()
                pyautogui.keyUp('ctrl')
                pyautogui.press('esc')
                #klikkaa lipasta repussa
               # pyautogui.click(879, 507, button='right')
                # klikkaa unload ammo
                time.sleep(0.5)
               # pyautogui.click(889, 416)
              #  pyautogui.moveTo(879, 507, 0.4)
                lipasreppu=imagesearcharea("lipasiso3.png", lipasC[0], lipasC[1], lipasC[2], lipasC[3], precision=0.5)
                if lipasreppu != [-1,-1]:
                    pyautogui.moveTo(lipasC[0]+lipasreppu[0]+5,lipasC[1]+lipasreppu[1]+5)
                    pyautogui.click(button='right')
                    pyautogui.click(lipasC[0] + lipasreppu[0] + 50, lipasC[1] + lipasreppu[1] - 88)
                    pyautogui.moveTo(lipasC[0] + lipasreppu[0] + 5, lipasC[1] + lipasreppu[1] + 5)



                pyautogui.dragTo(x1+40, y1+170+ylip,1.5)
                x1+=127
                x2+=127
                x5+51


        else:
             x1 += 127
             x2 += 127

def falmyynti():
    #FAL ase pystykuva koordinaatit ensimmainen
    x1=1254
    x2=1399
    y1=74
    y2=455
    #lippaan kuvan etsinnan koordinaatit
    x3=730
    x4= 952
    y3=713
    y4=923
    #toisen lippaan etsimisen koordit
    xx3=1299
    xx4= 1566
    yy3=725
    yy4= 926
    #lipas boksi repussa
    lipasC = [847, 370, 1161, 558]

    #ekan lippaan dragauskoordinaatit
    x5=1545
    y5=650
    #scrolli
    scrol = 3
    #%5 resetin jlk draggayskoordinaatit lippaasta aseeseen
    #uusi aseen koordinaatti lippaan draggaykseen
    ylip = 0
    #vaaka arvot falikuvan etsimiselle
    ax= 1264
    ay= 80
    ax2= 1641
    ay2= 205

   # pyautogui.click(x=1660, y=552)
    #jos haluaa klikata sivun ylös, spammii joku 4 kertaa
    pyautogui.click(1901, 93, 2)




    pyautogui.click(x=1660, y=552)
    for i in range(1,35):
        pyautogui.scroll(1)
    pyautogui.moveTo(x=1899, y=406)
    pyautogui.dragTo(1887, 692, 2, button='left')
    print("moi")


    for i in range(0,20):
        print(i,"kierrokset vilisee silimissä")
        if i ==5:
            pyautogui.click(x=1660, y=552)
            for i in range(1, scrol+4):
                pyautogui.scroll(-1)
            # x akseli resetti
            x1 = 1254
            x2 = 1399
            scrol += 6
            #ylip += 375
        if i == 10:
            pyautogui.moveTo(x=1660, y=552)
            for i in range(1, 10):
                pyautogui.scroll(-1)
            x1 = 1264
            x2 = 1389
            y1= 179
            y2= 557
        if i == 15:
            x1 = 1264
            x2 = 1389
            y1= 556
            y2 = 934

        falkuva =imagesearcharea("falkuva1.png", x1, y1, x2, y2, precision=0.7, im=None)
        falkuvaextP =imagesearcharea("falextremepysty.png", x1, y1, x2, y2, precision=0.7, im=None)
        falkuvaextLP =imagesearcharea("lyhytfalP.png", x1, y1, x2, y2, precision=0.7, im=None)
        print(falkuva, falkuvaextLP, falkuvaextP)


        #PYSTYASENTOETSINTA
        if falkuva !=[-1,-1] or falkuvaextP != [-1,-1]or falkuvaextLP != [-1,-1]:
            print("normifal:", falkuva, " extreme:",falkuvaextP)
            pyautogui.click(x1+falkuva[0]+20,y1+falkuva[1]+20, button='right')
            time.sleep(0.2)
            ins = (imagesearch("inspect.png", precision=0.5))
            print("inspectikuva: ",ins)
            time.sleep(0.2)

            pyautogui.click(ins[0] + 2, ins[1] + 5)
            time.sleep(0.3)
            lipas= imagesearcharea("lipas.png",x3, y3, x4, y4)



            print(lipas)


            if lipas[0]== -1:
                x1 += 127
                x2 += 127

                pyautogui.press('esc')
            if lipas[0] != -1:

                #lipas
               #lipas = imagesearcharea("lipas.png", x3, y3, x4, y4)
                # lippaan päälle hiiri
                pyautogui.moveTo(x3 + lipas[0] + 3, y3 + lipas[1] + 3, 0.5)
                pyautogui.keyDown('ctrl')
                pyautogui.click()
                pyautogui.keyUp('ctrl')
                pyautogui.press('esc')
                #pyautogui.click(879, 507, button='right')
                # klikkaa unload ammo
                time.sleep(0.3)
               # pyautogui.click(889, 416)
               # pyautogui.moveTo(879, 507, 0.4)
                lipasreppu = imagesearcharea("lipasiso3.png", lipasC[0], lipasC[1], lipasC[2], lipasC[3], precision=0.5)
                if lipasreppu != [-1, -1]:
                    pyautogui.moveTo(lipasC[0] + lipasreppu[0] + 5, lipasC[1] + lipasreppu[1] + 5)
                    pyautogui.click(button='right')
                    pyautogui.click(lipasC[0] + lipasreppu[0] + 50, lipasC[1] + lipasreppu[1] - 88)
                    pyautogui.moveTo(lipasC[0] + lipasreppu[0] + 5, lipasC[1] + lipasreppu[1] + 5)

                    pyautogui.dragTo(x1+40, y1+170+ylip,1.5)
                x1+=127
                x2+=127
                x5+51


        else:
             x1 += 127
             x2 += 127




    falmyynti2()
    vaaka()
    ammukset()










#vaaka()

falmyynti()





#ammukset()


#
# x = pytesseract.image_to_string(Image.open('imi.png'), lang='blight')
#
# print(x)
#y = int(x)
#ammokuvan boksi
# x1 = 847
# x2 = 910
# y1 = 441
# y2 = 506
# #tesseract
# x4 = 890
# y4 = 489
# x5 = 912
# y5 = 505
# #im = ImageGrab.grab(bbox=(x4, y4, x5, y5))
# im = ImageGrab.grab(bbox=(1162, 483, 1195, 505))
# im.save('im.png')
# x = pytesseract.image_to_string(Image.open('im.png'), lang='pubg')
#
# print(x)