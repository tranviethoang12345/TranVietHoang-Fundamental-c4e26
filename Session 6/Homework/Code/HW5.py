from turtle import *

def draw_star(length, x, y):
    penup()
    goto(x, y)
    pendown()
    angle = 180 - (180 / 5)
    for i in range(5):
        forward(length)
        right(angle)

draw_star(100,0,0)