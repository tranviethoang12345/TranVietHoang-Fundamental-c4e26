from turtle import *

speed(0)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

for j in range(5):
    begin_fill()
    for i in range(2):
        fd(50)
        lt(90)
        fd(100)
        lt(90)
    fillcolor(colors[j])
    fd(50)
    end_fill()

mainloop()