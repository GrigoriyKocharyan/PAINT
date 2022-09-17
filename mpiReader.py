from pygame import *
import time as t
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file = open("MyFile.mpi", 'r')
fr = file.read()

Pixels = []

init()
win = display.set_mode((755,685))

class Pixel:
    def __init__(self, x,y, win, size,r,g,b, is_earser):
        self.x = x
        self.y = y
        self.win = win
        self.size = size
        self.is_earser = is_earser
        self.r,self.g,self.b = r,g,b
    def draw(self):
        if self.is_earser: draw.rect(self.win, (255,255,255), (self.x, self.y, self.size, self.size))
        else: draw.rect(self.win, (self.r, self.g, self.b), (self.x, self.y, self.size, self.size))


for l in range(len(fr)):
    print(fr[l])
    if fr[l] == 'x':
        Pixels.append(Pixel(fr[l+1], 100, win, 10, 10, 20, 30, 0))


while True:
    m = mouse.get_pos()

    win.fill((235,235,235))
    for i in event.get():
        if i.type == QUIT:
            exit()
        '''if i.type == MOUSEBUTTONDOWN:
            if BUTTON_LEFT:
                clicked = 1
        if i.type == MOUSEBUTTONUP:
            clicked = 0'''

    draw.rect(win, (255, 255, 255), (0, 0, 770, 700))




    display.flip()