from turtle import *
# from HW3 import draw_square
def draw_square(y, x):
    for i in range(4):
        color(x)
        forward(y)
        right(90)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop ()