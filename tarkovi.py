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


def terminate():
    time.sleep(2)
    os.system("taskkill /im escapeFromTarkov.exe /f")
    k = imagesearch_loop1('terminateconf.png', 1, precision=0.8)
    pyautogui.moveTo(k[0]+94,k[1]+224)
    pyautogui.click()
    time.sleep(5)
    pyautogui.click(None, None)



def bckenderror():
    # onko = imagesearcharea("backenderror.png", 724, 473, 1191, 607, precision=0.8, im=None)
    onko1 = imagesearch('backenderror.png', precision=0.8)


# bckenderror()
# terminate()
def myynti():
    # add offer

    pyautogui.moveTo(1305, 81, 1)
    pyautogui.click(x=1305, y=81)
    time.sleep(0.5)
    # katso nimi
    pyautogui.moveTo(533, 649, 1)
    time.sleep(3)
    imse = imagesearchareaT('ds arms sa tuotekuva.png', 512, 607, 745, 691, precision=0.8, im=None)
    if imse == True:
        print('moi')
        # klikkaa asetta
        pyautogui.moveTo(609, 638, 1)
        pyautogui.click(x=609, y=638)
        time.sleep(1.5)
        # klikkaa plussaa
        pyautogui.moveTo(1460, 503, 1)
        pyautogui.click(x=1460, y=503)
        time.sleep(1.5)
        # etsii requirements ikkunan left top coordinatet
        koordit = (imagesearch('addr.png', precision=0.8))
        # x ja y cordsejen muutos vahan oikealle alas
        ekaa = koordit[0] + 10
        tokaa = koordit[1] + 15
        print(("spawnipointti", imagesearch('addr.png', precision=0.8)))
        # laittaa hiiren ikkunan draggays kohdalle
        pyautogui.moveTo(ekaa, tokaa)
        time.sleep(1)
        # draggaa keskelle
        pyautogui.dragTo(862, 249, 1, button='left')
        endpointti = (imagesearch('addr.png', precision=0.8))

        # klikkaa hintaikkunaa
        pyautogui.moveTo(endpointti[0] + 193, endpointti[1] + 44, 1)
        pyautogui.click(endpointti[0] + 193, endpointti[1] + 44)
        time.sleep(0.5)
        pyautogui.write("52500")
        time.sleep(0.5)
        time.sleep(1)
        pyautogui.moveTo(endpointti[0] + 217, endpointti[1] + 748, 1)
        pyautogui.click(endpointti[0] + 217, endpointti[1] + 748)
        #  pyautogui.moveTo(endpointti[0] + 217, endpointti[1] +748)
        pyautogui.moveTo(1277, 888, 1)
        pyautogui.click(x=1277, y=888)

        print('myy')

    else:
        # ristiloc=imagesearcharea('redcross.png', 1402, 154, 1526, 256, precision=0.8, im=None)
        pyautogui.click(x=1497, y=157)
    # pyautogui.click(x=1497, y=176)


def kokoFAL():
    if keyboard.is_pressed('b'):
        sys.exit()
    #  montako = 0
    # yhteishinta = 0
    # kokotesti()
    kierrokset = 1

   # kokotesti()
    halvat = 0
    for x in range(1, 50000):
        if keyboard.is_pressed('b'):
            sys.exit()

        kierrokset = kierrokset + 1
        print('kierros:', kierrokset)

        if kierrokset % 10 == 0:
            if imagesearch('backenderror.png', precision=0.8) != [-1, -1]:
                pyautogui.press('esc')

            if imagesearch('outofstock.png', precision=0.8) != [-1, -1]:
                pyautogui.press('esc')
            if imagesearch('offernotfound.png', precision=0.8) != [-1, -1]:
                pyautogui.press('esc')
            if imagesearch('etusivu.png', precision=0.8) != [-1, -1]:
                # klikkaa trading
                pyautogui.moveTo(950, 798, 1)
                pyautogui.click(None, None)
                # pyautogui.click(x=950, y=798)
                # time.sleep(3)
                # klikkaa flea market
                pyautogui.moveTo(953, 37, 1)
                pyautogui.click(None, None)
                # pyautogui.click(x=953, y=37)
                #   time.sleep(2)
                # klikkaa weapons
                pyautogui.moveTo(81, 270, 1)
                pyautogui.click(None, None)
                # pyautogui.click(x=81, y=270)
                # time.sleep(2)
                # klikkaa assault rifles
                pyautogui.moveTo(110, 332, 1)
                pyautogui.click(None, None)
                # pyautogui.click(x=110, y=332)
                #    time.sleep(2)
                # klikkaa fal
                pyautogui.moveTo(172, 767, 1)
                pyautogui.click(None, None)
                kokotesti()

        # if montako>= 5:
        # print(montako)
        # break
        print("________________________________")
        try:
            # error1()
            pyautogui.click(x=1324, y=130)
            # time.sleep((random.randint(0.29, 0.35)))
            time.sleep(0.25)
            # estii "PURCHASE" kuvaa jonka perusteella tietaa sivun ladanneen
            #  imagesearch_loop('osto.png', 0.1, 1645, 172, 1856, 245, precision=0.8, im=None, )

            # if imagesearchareaT('nuoli.png', 1343, 149, 1362, 164, precision=0.8, im=None)==True:

            if (os.path.exists(r'C:\Users\Aleksi\PycharmProjects\tesspython3\im.png')):
                os.remove("im.png")
            # im = ImageGrab.grab(bbox=(1260, 160, 1368, 188))
            # factory exit key
            # im = ImageGrab.grab(bbox=(1260, 160, 1374, 188))
            # alle50()
            im = ImageGrab.grab(bbox=(1243, 157, 1430, 190))
            # alle50()
            im.save('im.png')
            x = pytesseract.image_to_string(Image.open('im.png'), lang='pubg')
            x = x.replace(" ", "")
            x = x.replace('P', "")
            print(x)
            y = int(x)
            print("Hinta: " + str(y))
            if (y <= 46200):
                # imagesearch_loop('osto.png', 0.1, 1645, 172, 1856, 245, precision=0.8, im=None,)
                while True:
                    pyautogui.click(x=1747, y=182)
                    if keyboard.is_pressed('b'):
                        sys.exit()
                    if imagesearch('itempurchase.png') != [-1, -1]:
                        pyautogui.press('y')
                        break

                # time.sleep(0.05)
                # pyautogui.click(x=1747, y=182)
                # time.sleep(0.05)
                # pyautogui.press('y')
                # time.sleep(1)
                #  im.save('halpa' + str(kierrokset) + '.png')
                im.save(r'C:\Users\Aleksi\PycharmProjects\tesspython3\halvat\halpa' + str(kierrokset) + '.png')
                print('halpa')
                halvat += 1

                # montako = montako + 1
                # yhteishinta = yhteishinta + y
                # print(yhteishinta)
                playsound('ding2.mp3', False)

                # myynti()
            # kokotesti()
            # else:
            # print('kallis')
            print("Halpoja nakynyt:" + str(halvat))




        # elif imagesearch_loop('nuoli.png', 1343, 149, 1362, 164, precision=0.8, im=None)==True:
        #    print("vaaran")

        except ValueError:
            print("Ei tunnista.")


def kokoFACT_KEY():
    if keyboard.is_pressed('b'):
        sys.exit()
    kierrokset = 1
    #kokotestiExit()
    halvin = 10000000
    halvat = 0

    for x in range(1, 45000):
        if keyboard.is_pressed('b'):
            sys.exit()

        kierrokset = kierrokset + 1
        print('kierros:', kierrokset)

        if kierrokset % 10 == 0:
            if imagesearch('backenderror.png', precision=0.8) != [-1, -1]:
                pyautogui.press('esc')
            elif imagesearch('outofstock.png', precision=0.8) != [-1, -1]:
                pyautogui.press('esc')
            elif imagesearch('offernotfound.png', precision=0.8) != [-1, -1]:
                pyautogui.press('esc')
            elif imagesearch('etusivu.png', precision=0.8) != [-1, -1]:

                if imagesearch('etusivu.png', precision=0.8) != [-1, -1]:
                    factkeyflea()

            # error1()
        print("________________________________")

        # try:
        pyautogui.click(x=1324, y=130)
        time.sleep(0.1)
        # estii "PURCHASE" kuvaa jonka perusteella tietaa sivun ladanneen
        # imagesearch_loop('osto.png', 0.001, 1645, 172, 1856, 245, precision=0.8, im=None, )
        #jos kauppa ei ehdi lataamaan ennen kuvan ottamista, looppaa kunnes kuvan hinta saadaan int muotoon
        loopk = 0
        while True:
            loopk +=1

            if keyboard.is_pressed('b'):
                sys.exit()
            if loopk >10:
                break


            try:
                # if #(os.path.exists(r'C:\Users\Aleksi\PycharmProjects\tesspython3\im.png')):
                # os.remove("im.png")
                # factory exit key
                im = ImageGrab.grab(bbox=(1243, 157, 1430, 190))
                im.save('im.png')
                x = pytesseract.image_to_string(Image.open('im.png'), lang='pubg')
                x = x.replace(" ", "")
                x = x.replace('P', "")
                y = int(x)

                print("Hinta: " + str(y))
                if (y <= 48000):
                    wh = 0


                    while True:
                        wh += 1
                        pyautogui.click(x=1747, y=182)
                        if keyboard.is_pressed('b'):
                            sys.exit()
                        if imagesearch('itempurchase.png') != [-1, -1] or wh > 20:
                            pyautogui.press('y')
                            time.sleep(1)
                            if imagesearch('backenderror.png', precision=0.8) != [-1, -1]:
                                pyautogui.press('esc')
                            elif imagesearch('outofstock.png', precision=0.8) != [-1, -1]:
                                pyautogui.press('esc')
                            elif imagesearch('offernotfound.png', precision=0.8) != [-1, -1]:
                                pyautogui.press('esc')

                            break

                    im.save(r'C:\Users\Aleksi\PycharmProjects\tesspython3\halvat1\halpaexit' + str(kierrokset) + '.png')
                    print('halpa')
                    halvat += 1
                    playsound('ding2.mp3', False)
                    if (halvin > y):
                        halvin = y

                        print("Halpoja nakynyt:" + str(halvat))
                        print("Halvin:" + str(halvin))
                    break
                else:
                    break

            except ValueError:
                print("Ei tunnista.")

def kokoFACT_KEYV2():
    if keyboard.is_pressed('b'):
        sys.exit()
    kierrokset = 1
    halvat = 0

    for x in range(1, 60000):
        if keyboard.is_pressed('b'):
            sys.exit()

        kierrokset = kierrokset + 1
        print('kierros:', kierrokset)
        print("Halpoja nakynyt:" + str(halvat))

        if kierrokset % 30 == 0:
            if imagesearch('backenderror.png', precision=0.8) != [-1, -1]:
                pyautogui.press('esc')
            elif imagesearch('outofstock.png', precision=0.8) != [-1, -1]:
                pyautogui.press('esc')
            elif imagesearch('offernotfound.png', precision=0.8) != [-1, -1]:
                pyautogui.press('esc')
            elif imagesearch('etusivu.png', precision=0.8) != [-1, -1]:

                if imagesearch('etusivu.png', precision=0.8) != [-1, -1]:
                    factkeyflea()

            # error1()
        print("________________________________")

        # try:
        pyautogui.click(x=1324, y=130)
        time.sleep(0.16)
        # estii "PURCHASE" kuvaa jonka perusteella tietaa sivun ladanneen
        # imagesearch_loop('osto.png', 0.001, 1645, 172, 1856, 245, precision=0.8, im=None, )
        # jos kauppa ei ehdi lataamaan ennen kuvan ottamista, looppaa kunnes kuvan hinta saadaan int muotoon



        #kolmas = imagesearchareaT('avainkuva1.png', 801, 141, 878, 217, precision=0.8, im=None)
        #toka = imagesearchareaT('locked1.png', 1651, 150,1825, 207,precision=0.8, im=None)
        eka = imagesearch('osto.png')


        if eka != [-1, -1]:# or toka or kolmas:
            playsound('ding2.mp3', False)

            wh = 0
            while wh < 1:
                wh += 1
                pyautogui.click(x=1747, y=182)
                pyautogui.press('y')
                pyautogui.press('y')
               # playsound('ding2.mp3', False)
                #time.sleep(0.01)

            #time.sleep(0.26)
            if imagesearch('backenderror.png', precision=0.8) != [-1, -1]:
                pyautogui.press('esc')
            elif imagesearch('outofstock.png', precision=0.8) != [-1, -1]:
                pyautogui.press('esc')
            elif imagesearch('offernotfound.png', precision=0.8) != [-1, -1]:
                pyautogui.press('esc')



            # im.save(r'C:\Users\Aleksi\PycharmProjects\tesspython3\halvat1\halpaexit' + str(kierrokset) + '.png')
            print('halpa')
            halvat += 1
            #playsound('ding2.mp3', False)

            #print("Halvin:" + str(halvin))

       # if toka:
            #playsound('ding2.mp3', False)

def factkeyflea():
    # klikkaa trading
    pyautogui.moveTo(950, 798, 1)
    pyautogui.click(None, None)
    # klikkaa flea market
    pyautogui.moveTo(953, 37, 1)
    pyautogui.click(None, None)
    # klikkaa searchbox
    pyautogui.moveTo(132, 121, 1)
    pyautogui.click(None, None)
    # kirjoittaa ja klikkaa
    pyautogui.typewrite("Factory exit key", interval=0.2)
    #  pyautogui.typewrite()
    time.sleep(0.5)
    pyautogui.click(x=158, y=167)


# kokotestiExit()
# factkeyflea()
def kokokuvatesti():
    im = ImageGrab.grab(bbox=(1260, 160, 1371, 188))
    im.save('im.png')
    x = pytesseract.image_to_string(Image.open('im.png'))
    print(x)
    x = x.replace(" ", "")
    print(x)


def kokotesti():
    time.sleep(1)
    pyautogui.click(x=1363, y=24)
    pyautogui.moveTo(x=838, y=177)
    time.sleep(3)
    imse1 = imagesearchareaT('ds arms sa tuotekuva.png', 831, 125, 1014, 187, precision=0.8, im=None)
    if imse1 == True:
        print('oikee sivu')
        return True
    # print('ei exitannu')
    else:
        print('väärä sivu')
        sys.exit()

def restart():
    time.sleep(0.3)
    pyautogui.click(x=482, y=85)
    time.sleep(0.2)
    pyautogui.click(x=795, y=146)
    pyautogui.typewrite("0")
    time.sleep(0.2)
    pyautogui.click(x=609, y=425)
    time.sleep(0.5)
    pyautogui.press('f5')
    pyautogui.click(x=169, y=126)
    time.sleep(0.3)
    pyautogui.typewrite("factory exit key", interval= 0.2)
    time.sleep(0.2)
    pyautogui.click(x=188, y=165)
    time.sleep(0.2)
    pyautogui.click(x=482, y=85)
    time.sleep(0.2)
    pyautogui.click(x=795, y=146)
    time.sleep(0.2)
    pyautogui.typewrite("100000")
    time.sleep(0.2)
    pyautogui.click(x=609, y=425)
# x3=646
# x4= 1026
# y3=780
# y4=914
# lipas= imagesearcharea("lipas.png",x3, y3, x4, y4)
# print(lipas)646 780
def falmyynti():
    #FAL ase pystykuva koordinaatit ensimmainen
    x1=1254
    x2=1399
    y1=74
    y2=455
    #lippaan kuvan etsinnan koordinaatit
    x3=646
    x4= 1026
    y3=780
    y4=914
    #ekan lippaan dragauskoordinaatit
    x5=1545
    y5=650
    #scrolli
    scrol = 3
    #%5 resetin jlk draggayskoordinaatit lippaasta aseeseen
    #uusi aseen koordinaatti lippaan draggaykseen
    ylip = 0

    pyautogui.click(x=1660, y=552)
    for i in range(1,20):
        pyautogui.scroll(1)
    pyautogui.moveTo(x=1899, y=406)
    pyautogui.dragTo(1887, 692, 2, button='left')

    for i in range(0,6):
        print(i)
        if i % 5 == 0 and i != 0:
            pyautogui.click(x=1660, y=552)
            for i in range(1, scrol+4):
                pyautogui.scroll(-1)
            # x akseli resetti
            x1 = 1254
            x2 = 1399
            scrol += 6
            ylip += 375
        falkuva =imagesearcharea("falkuva1.png", x1, y1, x2, y2, precision=0.7, im=None)



        print(falkuva)
        if falkuva !=[-1,-1]:
            pyautogui.click(x1+falkuva[0],y1+falkuva[1], button='right')
            print("löyty pysty")
            time.sleep(0.2)
            ins = (imagesearch("inspect.png", precision=0.5))
            time.sleep(0.2)
            pyautogui.click(ins[0] + 2, ins[1] + 2)
            time.sleep(0.2)
            lipas= imagesearcharea("lipas.png",x3, y3, x4, y4)
            print(lipas)

               # pyautogui.click(x3+lipas[0]+3,y3+ lipas[1]+3,button='right')
            if lipas[0]== -1:
                x1 += 127
                x2 += 127

                pyautogui.press('esc')
            if lipas[0] != -1:

                for i in range(1, scrol):
                    pyautogui.moveTo(x=1693, y=405)
                    pyautogui.scroll(1)
                #lippaan päälle hiiri
                pyautogui.moveTo(x3+lipas[0]+3,y3+ lipas[1]+3,0.5)
                #vetaa lippaan stashiin
                #pyautogui.dragTo(1545, 143, 2)
                pyautogui.dragTo(1128, 631,2)
               # pyautogui.click(1545, 143, button= 'right')
                pyautogui.click(1128, 631, button= 'right')
                #klikkaa unload ammo
              #  pyautogui.click(1545+20, 143-73)
                pyautogui.click(1128+20, 631-73)
                pyautogui.press('esc')
                #pyautogui.press('esc')
                #pyautogui.moveTo(1545, 143,0.4)
              #  pyautogui.dragTo(1128, 631,2)
                pyautogui.dragTo(x1+40, y1+170+ylip,1)
                x1+=127
                x2+=127
                x5+51

                for i in range(1,scrol):
                    pyautogui.scroll(-1)

        else:
            break


#falmyynti()




def kokotestiExit():
    time.sleep(1)
    pyautogui.click(x=1363, y=24)
    pyautogui.moveTo(x=838, y=177)
    time.sleep(3)
    imse1 = imagesearchareaT('factoryexit.png', 831, 125, 1014, 187, precision=0.8, im=None)
    if imse1 == True:
        print('oikee sivu')
        return True
    # print('ei exitannu')
    else:
        print('väärä sivu')
        sys.exit()


def loopexit():
    while True:
        time.sleep(0.1)
        print('paalla')
        if keyboard.is_pressed('b'):
            sys.exit()


def hintatesti():
    # im = ImageGrab.grab(bbox=(1260, 160, 1368, 188))
    # lappari
    im = ImageGrab.grab(bbox=(1243, 157, 1430, 190))
    # alle50()
    im.save('im.png')
    x = pytesseract.image_to_string(Image.open('im.png'), lang='pubg')
    x = x.replace(" ", "")
    x = x.replace('P', "")
    print(x)


#  y = int(x)
def errorExit():
    terminate()
    time.sleep(5)
    subprocess.call(['C:\Battlestate Games\BsgLauncher\BsgLauncher.exe'])
    pelinappula = imagesearch_loop1('playbtn.png', 1, precision=0.8)
    # click_image('playbtn.png', pelinappula, "left", 1)
    # pyautogui.click(pelinappula[0]+10, pelinappula[1]+10)
    pyautogui.moveTo(pelinappula[0] + 10, pelinappula[1] + 10, 1)
    pyautogui.click(None, None)
    # etsii kunnes etusivu aukeaa
    imagesearch_loop1('etusivu.png', 10, precision=0.8)
    # klikkaa trading
    pyautogui.moveTo(950, 798, 1)
    pyautogui.click(None, None)
    # klikkaa flea market
    pyautogui.moveTo(953, 37, 1)
    pyautogui.click(None, None)
    # klikkaa searchbox
    pyautogui.moveTo(132, 121, 1)
    pyautogui.click(None, None)
    # kirjoittaa ja klikkaa
    pyautogui.typewrite("Factory exit key")
    pyautogui.click(x=158, y=167)

def errorExitV2():
    terminate()
    time.sleep(5)
    subprocess.call(['C:\Battlestate Games\BsgLauncher\BsgLauncher.exe'])
    pelinappula = imagesearch_loop1('playbtn.png', 1, precision=0.8)
    # click_image('playbtn.png', pelinappula, "left", 1)
    # pyautogui.click(pelinappula[0]+10, pelinappula[1]+10)
    pyautogui.moveTo(pelinappula[0] + 10, pelinappula[1] + 10, 1)
    pyautogui.click(None, None)
    # etsii kunnes etusivu aukeaa
    imagesearch_loop1('etusivu.png', 10, precision=0.8)
    # klikkaa trading
    pyautogui.moveTo(950, 798, 1)
    pyautogui.click(None, None)
    # klikkaa flea market
    pyautogui.moveTo(953, 37, 1)
    pyautogui.click(None, None)
    restart()

def valikkotesti():
    x = pytesseract.image_to_string(Image.open('asevalikkotesti.png'))
    print(x)
    # x = x.replace(" ", "")'


def osto_klikki():
    wh = 0;
    while True:
        wh += 1
        pyautogui.click(x=1747, y=182)
        if keyboard.is_pressed('b'):
            sys.exit()
        if imagesearch('itempurchase.png') != [-1, -1] or wh > 20:
            pyautogui.press('y')
            time.sleep(1)
            if imagesearch('backenderror.png', precision=0.8) != [-1, -1]:
                pyautogui.press('esc')
            if imagesearch('outofstock.png', precision=0.8) != [-1, -1]:
                pyautogui.press('esc')
            if imagesearch('offernotfound.png', precision=0.8) != [-1, -1]:
                pyautogui.press('esc')

            break


#restart()
#errorExitV2()
# osto_klikki()
# error1()
# hintatesti()
# kokoFAL()
#kokoFACT_KEY()
kokoFACT_KEYV2()
# hintatesti()
# x.replace(" ", "")
# errorExit()
# print(int(x))

# print(pytesseract.image_to_string(Image.open('im.png')))

# French text image to string
# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

# In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# NOTE: In this case you should provide tesseract supported images or tesseract will return error
# print(pytesseract.image_to_string('test2.png'))

# Batch processing with a single file containing the list of multiple image file paths
# print(pytesseract.image_to_string('images.txt'))

# Timeout/terminate the tesseract job after a period of time
# try:
# print(pytesseract.image_to_string('test.jpg', timeout=2)) # Timeout after 2 seconds
# print(pytesseract.image_to_string('test.jpg', timeout=0.5)) # Timeout after half a second
# except RuntimeError as timeout_error:
# Tesseract processing is terminated
#  pass

# Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open('test2.png')))

# Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open('test.png')))

# Get information about orientation and script detection
# print(pytesseract.image_to_osd(Image.open('test.png')))

# Get a searchable PDF
# pdf = pytesseract.image_to_pdf_or_hocr('test1.png', extension='pdf')
# with open('test1.pdf', 'w+b') as f:
#  f.write(pdf) # pdf type is bytes by default

# Get HOCR output
# hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')

#toka = imagesearchareaT('locked1.png', 1651, 150,1825, 207,precision=0.8, im=None)
#print(toka)


#k[0]+=94
#k[1]+=224



#os.system("taskkill /im escapeFromTarkov.exe /f")