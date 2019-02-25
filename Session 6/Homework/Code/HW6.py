from turtle import *
from HW5 import draw_star

speed(0)
color("blue")
def draw_star(length, x, y):
    penup()
    goto(x, y)
    pendown()
    angle = 180 - (180 / 5)
    for i in range(5):
        forward(length)
        right(angle)


for i in range(100):
    import random
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    length = random.randint(3,10)
    draw_star(x,y,length)
