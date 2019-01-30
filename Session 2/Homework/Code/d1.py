from turtle import *

speed(0)

shape('arrow')

color("red")

for i in range(4):
    for i in range (2):
        left(30)
        forward(100)
        right(60)
        forward(100)
        right(150)   
    left(90)     
mainloop()