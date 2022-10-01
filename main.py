from pygame import *
import time as t
import os
import re

saved2 = 0


red = 0
blue = 0
cs = 0
green = 0
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ggg = 680
yyy = 680
PixelsS = ''
Pixels = []
files = ''
bbb = 680

def colorSelect(yyy,redtt,cs,ggg,redtttt,redtttt2,bbb,red,green,blue):
    draw.rect(win, (235, 235, 235), (25, 480, 200, 250), 100, 10)
    draw.rect(win, (215, 215, 215), (25, 480, 200, 250), 3, 10)

    draw.rect(win, (215, 100, 100), (25+20, 480+20, 15, 200), 3, 10)
    draw.rect(win, (100, 215, 100), (25 + 60, 480 + 20, 15, 200), 3, 10)
    draw.rect(win, (100, 100, 215), (25 + 100, 480 + 20, 15, 200), 3, 10)

    draw.rect(win, (red, green, blue), (25 + 100+50, 480 + 20, 30, 200), 0, 15)
    draw.rect(win, (red/1.4, green/1.4, blue/1.4), (25 + 100 + 50, 480 + 20, 30, 200), 3, 15)

    draw.rect(win, (255, 0, 0), (25 + 18, yyy, 19, 19), 0, 10)
    draw.rect(win, (215,100, 100), (25 + 18, yyy, 19, 19), 3, 10)
    win.blit(redtt, (-redtt.get_rect()[2]/2+53,705))

    draw.rect(win, (0, 255, 0), (25 + 18+19+19+2, ggg, 19, 19), 0, 10)
    draw.rect(win, (100, 215, 100), (25 + 18+19+19+2, ggg, 19, 19), 3, 10)
    win.blit(redtttt, (-redtttt.get_rect()[2] / 2 + 53+38, 705))

    draw.rect(win, (0, 0, 255), (25 + 18 + 19 + 19 + 2+38+2, bbb, 19, 19), 0, 10)
    draw.rect(win, (100, 100, 215), (25 + 18 + 19 + 19 + 2+38+2, bbb, 19, 19), 3, 10)
    win.blit(redtttt2, (-redtttt2.get_rect()[2] / 2 + 53 + 38+39+2, 705))


    #return ggg, bbb,yyy
    #return bbb
    #return yyy


    #display.flip()


sfile = open("MyFile.mpi", 'w+', encoding='utf-8')

def fileSave():

    sfile.write(str(PixelsS))


p = image.load("pencil.png")
p = transform.smoothscale(p, (25, 25))
e = image.load("earser.png")
e = transform.smoothscale(e, (25, 25))
pencil = 1
clicked = 0
size = 10
r, g, b = 40, 0, 50

init()
win = display.set_mode((800, 800))

redt = font.SysFont('Lucida Console', 15,1,0)
redtt = redt.render(str(red), 1, (0, 0, 0))
redtttt = redt.render(str(green), 1, (0, 0, 0))
redtttt2 = redt.render(str(blue), 1, (0, 0, 0))

class Pixel:
    def __init__(self, x, y, win, size, r, g, b, is_earser):
        self.x = x
        self.y = y
        self.win = win
        self.size = size
        self.is_earser = is_earser
        self.r, self.g, self.b = r, g, b
    def draw(self):
        if self.is_earser:
            draw.rect(self.win, (255, 255, 255), (self.x+self.size/2, self.y, self.size, self.size))
        else:
            draw.rect(self.win, (self.r, self.g, self.b), (self.x+self.size/2, self.y, self.size, self.size))



while True:
    m = mouse.get_pos()

    win.fill((235,235,235))
    draw.rect(win, (255, 255, 255), (15+35, 15, 700, 700))

    if cs == 1:
        red = int(-yyy * 1.39+683+266+1)
        green = int(-ggg * 1.39 + 683 + 266 + 1)
        blue = int(-bbb * 1.39 + 683 + 266 + 1)

        redtt = redt.render(str(red), 1, (0, 0, 0))
        redtttt = redt.render(str(green), 1, (0, 0, 0))
        redtttt2 = redt.render(str(blue), 1, (0, 0, 0))

    print(redtt.get_rect())
    for i in event.get():
        if i.type == QUIT:
            exit()
        if i.type == MOUSEBUTTONDOWN:
            if BUTTON_LEFT:
                clicked = 1
        elif i.type == KEYDOWN:
            if K_0:
                saved2 = 1

        if i.type == MOUSEBUTTONUP:
            clicked = 0

    xx = round(m[0]/size)*size-size/2
    yy = round(m[1]/size)*size-size/2
    if saved2==0:
        draw.rect(win, (200,200,200), (15,730, 770,60), 5, 20)
    for pix in Pixels:
        pix.draw()

    if mouse.get_pressed()[0]:
        if mouse.get_pos()[0] >= 25 + 18 and mouse.get_pos()[0] <= 25 + 18 +19 and cs:
            yyy = min(max(500, mouse.get_pos()[1]), 480 + 203)
            if mouse.get_pressed()[0] and cs:
                yyy = min(max(500, mouse.get_pos()[1]), 480 + 203)
        if mouse.get_pos()[0] >= 25 + 18+19+19 and mouse.get_pos()[0] <= 25 + 18 + 19+18+19 and cs:
            ggg = min(max(500, mouse.get_pos()[1]), 480 + 203)
        if mouse.get_pos()[0] >= 25 + 18+19+19+38 and mouse.get_pos()[0] <= 25 + 18 + 19+18+19+38 and cs:
            bbb = min(max(500, mouse.get_pos()[1]), 480 + 203)






    if m[0] >= 25 and m[0] <= 65 and m[1] >= 740 and m[1] <= 780:
        draw.rect(win, (220, 220, 220), (25, 740, 40, 40), 100, 10)
        if clicked:
            clicked = 0
            pencil = 1
    if m[0] >= 25+50 and m[0] <= 65+50 and m[1] >= 740 and m[1] <= 780:
        draw.rect(win, (220, 220, 220), (25+50, 740, 40, 40), 100, 10)
        if clicked:
            clicked = 0
            pencil = 0
    if m[0] >= 25+710 and m[0] <= 65+710 and m[1] >= 740 and m[1] <= 780:
        draw.rect(win, (220, 220, 220), (25+710, 740, 40, 40), 100, 10)
        if clicked:
            clicked = 0
            fileSave()
    if m[0] >= 25+100 and m[0] <= 65+100 and m[1] >= 740 and m[1] <= 780:
        draw.rect(win, (220, 220, 220), (25+100, 740, 40, 40), 100, 10)
        if clicked:
            clicked = 0
            if cs == 0:
                cs = 1
            else:
                cs = 0


    if cs:
        colorSelect(yyy,redtt,cs,ggg,redtttt,redtttt2,bbb,red,green,blue)

    if saved2 == 0:
        if pencil == 1:
            draw.rect(win, (190, 190, 190), (25, 740, 40, 40), 100, 10)
        if pencil == 0:
            draw.rect(win, (190, 190, 190), (25+50, 740, 40, 40), 100, 10)


        draw.rect(win, (100, 100, 100), (25, 740, 40, 40), 3, 10)
        draw.rect(win, (100, 100, 100), (25+50, 740, 40, 40), 3, 10)
        draw.rect(win, (100, 100, 100), (25 + 710, 740, 40, 40), 3, 10)
        draw.rect(win, (100, 100, 100), (25 + 100, 740, 40, 40), 3, 10)

    if saved2 == 0:
        if yy >= 15 and yy <= 710 and xx >= 40 and xx <= 775-35:
            if cs ==0:
                draw.rect(win, (0, 0, 0), (round(m[0] / size) * size , round(m[1] / size) * size - size / 2, size, size), 1)

            if cs == 1:
                mouse.set_visible(True)
            if cs == 0:
                mouse.set_visible(False)
                draw.rect(win, (255, 255, 255), (round(m[0] / size) * size + 1, round(m[1] / size) * size - size / 2 + 1, size - 2, size - 2), 1)

            if mouse.get_pressed()[0] and cs == 0:
                Pixels.append(Pixel(xx, yy, win, size, red, green, blue, -pencil+1))

                PixelsS += ("x:"+ str(int(xx)) + ",")
                PixelsS += ("y:" + str(int(yy)) + ",")
                PixelsS += ("r:" + str(int(r)) + ",")
                PixelsS += ("g:" + str(int(g)) + ",")
                PixelsS += ("b:" + str(int(b)) + ",")
                PixelsS += ("p:" + str(int(pencil)) + ";")
                PixelsS += ("\n")


        else:
            mouse.set_visible(True)
    if saved2 == 0:
        win.blit(p, (33,747))
        win.blit(e, (33+50, 747))




    if saved2:
        saved2 = 0
        print(1)
        folder = os.path.join(os.path.dirname(__file__), 'screenshots')
        if not os.path.exists(folder):
            os.makedirs(folder)
        index = 0
        for f in os.listdir(folder):
            match = re.match('screenshot\d+.png', f)
            if match:

                new_index = int(re.search('\d+', f).group())
                index = max(index, new_index + 1)

        image.save(win,
                   os.path.join(folder, f'screenshot{index:03d}.png'))



    display.flip()
