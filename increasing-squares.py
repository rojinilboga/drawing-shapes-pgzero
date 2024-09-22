import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():
    screen.clear()
    r = randint(100,255)
    g = randint(5,255)
    b = randint(100,255)

    width = WIDTH
    height = HEIGHT - 200


    for i in range(15):
        box = Rect((0,0), (width,height))
        box.center = 150,150
        screen.draw.rect(box,(r,g,b))

        b +=9


        width +=7
        height +=10

pgzrun.go()



