import copy

import pyautogui
from pyautogui import *
import time
from PIL import Image
import random
import threading
import concurrent.futures

#click the next tile

xl, yl, wl, hl = pyautogui.locateOnScreen('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\top_left.png')
xr, yr, wr, hr = pyautogui.locateOnScreen('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\bottom_right.png')

#find width and height of area in order to decrease screenshot size and maximise speed
w = (xr + 10) - (xl - 10)
h = (yr + 10) - (yl - 10)

TILES = {
    '0': Image.open('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\land.png'),
    '.': Image.open('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\empty.png'),
    1: Image.open('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\1.png'),
    2: Image.open('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\2.png'),
    3: Image.open('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\3.png'),
    4: Image.open('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\4.png'),
    5: Image.open('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\5.png'),
    6: Image.open('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\6.png'),
    7: Image.open('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\7.png'),
    8: Image.open('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\8.png'),
    '!': Image.open('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\bomb2.png'),
    'B': Image.open('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\bomb1.png'),
    'F': Image.open('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\flag.png')
}



# CHANGE THIS TO 1 ONCE FINISHED TESTING vv
xy = 1

def find_tiles_for_tile(tile, xl, yl, w, h):
    positions = pyautogui.locateAllOnScreen(TILES[tile], region=(xl, yl, w, h), grayscale=True)
    return [{'value': tile, 'position': p} for p in positions]

max_threads = 16

def clicks(clicktype, tilelist, tilelist1):
    a = 0
    while a < 9:
        if clicktype == 'land':
            if tilelist[a]['value'] == '0':
                x1, y1, w1, h1 = tilelist[a]['position']
                pyautogui.click(x1, y1, button='right')
                print('RIGHTCLICK FOR FLAGS!!!')
                tilelist1[a]['value'] = 'F'

        if clicktype == 'flags':
            if tilelist[a]['value'] == '0':
                x1, y1, w1, h1 = tilelist[a]['position']
                pyautogui.click(x1, y1, button='left')
                print('LEFTCLICK LAND!!!')
                tilelist1[a]['value'] = '.'
        a += 1

#    for a in tilelist:
#        if clicktype == 'land':
#            if a['value'] == '0':
 #               x1, y1, w1, h1 = a['position']
 #               pyautogui.click(x1, y1, button='right')
 #               print('RIGHTCLICK FOR FLAGS!!!')
  #              a['value'] = 'F'
#
  #      if clicktype == 'flags':
   #         if a['value'] == '0':
   #             x1, y1, w1, h1 = a['position']
   #             pyautogui.click(x1, y1, button='left')
    #            print('LEFTCLICK LAND!!!')
   #             a['value'] = '.'

tiles = pyautogui.locateAllOnScreen('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\land.png')
tiles = list(tiles)


def initialbreak():
    tiles = pyautogui.locateAllOnScreen('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\land.png')
    tiles = list(tiles)
    all_tiles = []
        # ------------------


    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(find_tiles_for_tile, tile, xl, yl, w, h) for tile in TILES]
        for future in concurrent.futures.as_completed(futures):
            all_tiles.extend(future.result())

    all_tiles = sorted(all_tiles, key=lambda x: (x['position'][1], x['position'][0]))

    width = len(set([x['position'][0] for x in all_tiles]))
        # ------------------

    for ii, tile in enumerate(all_tiles):
        print(tile['value'], end=' ')
        if (ii + 1) % width == 0:
            print()

    tiles = sorted(tiles, key=lambda x: (x[1], x[0]))
    x, y = tiles[0][0] + 5, tiles[0][1] + 5

    pyautogui.click(x, y)

def solver():
    num = 0

    landamount = 0
    emptyamount = 0
    flags = 0
    boardstate = []
    tiles = pyautogui.locateAllOnScreen('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\land.png')
    tiles = list(tiles)

    all_tiles = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(find_tiles_for_tile, tile, xl, yl, w, h) for tile in TILES]
        for future in concurrent.futures.as_completed(futures):
            all_tiles.extend(future.result())

    all_tiles = sorted(all_tiles, key=lambda x: (x['position'][1], x['position'][0]))

    width = len(set([x['position'][0] for x in all_tiles]))

    # iterate from i = 0 to i = 3
    while (num <= 195):

        if len(boardstate) == 0 or (boardstate[num]['value'] != '.' and boardstate[num]['value'] != '0' and boardstate[num]['value'] != 'F'):
            #------------------



            #------------------

            for ii, tile in enumerate(all_tiles):
                print(tile['value'], end=' ')
                if (ii + 1) % width == 0:
                    print()

            tiles = sorted(tiles,key=lambda x: (x[1], x[0]))
            x, y = tiles[0][0]+5, tiles[0][1]+5

            boardstate = all_tiles

            #if xy == 2:
            #    boardstate = all_tiles
            #    xy += 1
            # if xy == 1:
            #    pyautogui.click(x, y)
            #    xy += 1

        #    aa = all_tiles[num-width-1]['value']
        #    ab = all_tiles[num-width]['value']
        #    ac = all_tiles[num-width+1]['value']
        #    ba = all_tiles[num - 1]['value']
        #    tilenumber = all_tiles[num]['value']
        #    bc = all_tiles[num + 1]['value']
        #    ca = all_tiles[num+width-1]['value']
        #    cb = all_tiles[num+width]['value']
        #    cc = all_tiles[num+width+1]['value']



            aa = copy.deepcopy(all_tiles[num - width - 1])
            aa1 = all_tiles[num - width - 1]
            ab = copy.deepcopy(all_tiles[num - width])
            ab1 = all_tiles[num - width]
            ac = copy.deepcopy(all_tiles[num - width + 1])
            ac1 = all_tiles[num - width + 1]
            ba = copy.deepcopy(all_tiles[num - 1])
            ba1 = all_tiles[num - 1]
            tilenumber = copy.deepcopy(all_tiles[num])
            tilenumber1 = all_tiles[num]
            print('TILENUMBER --')
            bc = copy.deepcopy(all_tiles[num + 1])
            bc1 = all_tiles[num + 1]

            if num + width >= 195:
                print(ca)
                print(cb)
                print(cc)

                ca['value'] = '0'
                ca1['value'] = '0'
                cb['value'] = '0'
                cb1['value'] = '0'
                cc['value'] = '0'
                cc1['value'] = '0'

                print('num + width > 195')

                print(ca)
                print(cb)
                print(cc)

            else:
                ca = copy.deepcopy(all_tiles[num + width - 1])
                ca1 = all_tiles[num + width - 1]
                cb = copy.deepcopy(all_tiles[num + width])
                cb1 = all_tiles[num + width]
                cc = copy.deepcopy(all_tiles[num + width + 1])
                cc1 = all_tiles[num + width + 1]
                print('CC --')
                print(ca)
                print(cb)
                print(cc)

            tileedge(num)

            if 'top' in tileedge(num):
                aa['value'] = '.'
                ab['value'] = '.'
                ac['value'] = '.'
            if 'bottom' in tileedge(num):
                ca['value'] = '.'
                cb['value'] = '.'
                cc['value'] = '.'
            if 'left' in tileedge(num):
                aa['value'] = '.'
                ba['value'] = '.'
                ca['value'] = '.'
            if 'right' in tileedge(num):
                ac['value'] = '.'
                bc['value'] = '.'
                cc['value'] = '.'



            tilelist = [aa,ab,ac,ba,tilenumber,bc,ca,cb,cc]
            tilelist1 = [aa1,ab1,ac1,ba1,tilenumber1,bc1,ca1,cb1,cc1]

            landamount = 0
            emptyamount = 0
            flags = 0

            for a in tilelist:
                if a['value'] == '0':
                    landamount += 1
                if a['value'] == '.':
                    emptyamount += 1
                if a['value'] == 'F':
                    flags += 1
                if tilenumber['value'] == 'B':
                    exit()

            if isinstance(tilenumber['value'], int):
                if (landamount + flags) <= int(tilenumber['value']):
                    print("\nFLAG EVERYTHING!\n")
                    clicks('land', tilelist, tilelist1)
                elif flags == int(tilenumber['value']):
                    print("\nBREAK EVERYTHING!\n")
                    clicks('flags', tilelist, tilelist1)


                #if landamount <= int(tilenumber):
                    #qqq = input("I am about to click on a bunch of tiles")
                    #xaa, yaa, waa, haa = all_tiles[num-width-1]['position']
                    #xab, yab, wab, hab = all_tiles[num-width]['position']
                    #xac, yac, wac, hac = all_tiles[num-width+1]['position']
                    #xba, yba, wba, hba = all_tiles[num-1]['position']
                    #xbc, ybc, wbc, hbc = all_tiles[num+1]['position']
                    #xca, yca, wca, hca = all_tiles[num+width-1]['position']
                    #xcb, ycb, wcb, hcb = all_tiles[num+width]['position']
                    #xcc, ycc, wcc, hcc = all_tiles[num+width+1]['position']


                #use value of above to check type of tile, then click or dont click dependent on flag or land


                    #pyautogui.click(xaa, yaa, button='right')
                    #pyautogui.click(xab, yab, button='right')
                    #pyautogui.click(xac, yac, button='right')
                    #pyautogui.click(xba, yba, button='right')
                    #pyautogui.click(xbc, ybc, button='right')
                    #pyautogui.click(xca, yca, button='right')
                    #pyautogui.click(xcb, ycb, button='right')
                    #pyautogui.click(xcc, ycc, button='right')

            print(num)
            print("Land: " + str(landamount))
            print("Empty: " + str(emptyamount))
            print("Flags: " + str(flags))
            print("Tile Number: " + str(tilenumber))
            print("All Tiles Number: " + str(all_tiles[num]))

            ##https: // www.w3schools.com / python / python_lists_loop.asp

            print(aa, ab, ac)
            print(ba, tilenumber, bc)
            print(ca, cb, cc)

            #speed link
            #https://stackoverflow.com/questions/72156405/locate-an-image-within-a-specific-region-of-the-screen-using-pythons-pyautogui

            print(x,y)
            #pyautogui.click(x, y)
            print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

        num = num + 1

def tileedge(num):
    width = 14

    returnvalue = ''
    if 0 <= num <= (width - 1):
        returnvalue += 'top'

    if 195 - (width - 1) <= num <= 195:
        returnvalue += 'bottom'

    if num % width == 0:
        returnvalue += 'left'

    if (num + 1) % width == 0:
        returnvalue += 'right'

    return returnvalue

initialbreak()

#bomb = []
#land = []

bomb = pyautogui.locateOnScreen('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\bomb1.png')
land = pyautogui.locateOnScreen('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\land.png')

while bomb == None and land != None:
    solver()
    bomb = pyautogui.locateOnScreen('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\bomb1.png')
    land = pyautogui.locateAllOnScreen('C:\\Users\\max\\OneDrive\\Desktop\\minesweeper sprites\\land.png')
    print(bomb)
    print(land)