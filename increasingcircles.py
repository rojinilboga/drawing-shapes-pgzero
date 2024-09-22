import pgzrun
from random import randint


WIDTH, HEIGHT = 640, 480

circle_x, circle_y = WIDTH // 2, HEIGHT // 2
circle_radius = 50

def draw():
    global circle_radius
    r = randint(50,255)
    g = randint(20,255)
    b = randint(10,255)
    screen.clear()
    for i in range (30):
        screen.draw.circle((circle_x, circle_y), circle_radius, (r,g,b))


        circle_radius += 5


pgzrun.go()
