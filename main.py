from pygame import *
import time as t

init()
win = display.set_mode((800,800))


class Object:
    def __init__(self, x,y, win):
        self.x = x
        self.y = y
        self.win = win
    def draw(self):
        draw.rect(self.win, (0, 0, 0), (self.x, self.y, 5, 5))



Objects = []

while True:
    m = mouse.get_pos()
    win.fill((255,255,255))



    for i in event.get():
        if i.type == QUIT:
            exit()
        if i.type == MOUSEBUTTONDOWN:
            if BUTTON_LEFT:
                clicked = 1
        if i.type == MOUSEBUTTONUP:
            clicked = 0

    xx = round(m[0]/5)*5-2.5
    yy = round(m[1]/5)*5-2.5

    draw.rect(win, (0,0,0), (round(m[0]/5)*5-2.5,round(m[1]/5)*5-2.5, 5,5), 1)
    if mouse.get_pressed()[0]:
        Objects.append(Object(xx, yy, win))
    for obj in Objects:
        obj.draw()

    display.flip()
