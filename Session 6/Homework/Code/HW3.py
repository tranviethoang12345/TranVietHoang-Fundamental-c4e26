from turtle import *
shape("turtle")
speed(0)

def draw_square(length, clr):
    for i in range(4):
        color(clr)
        forward(length)
        right(90)

draw_square(200,"blue")
mainloop ()