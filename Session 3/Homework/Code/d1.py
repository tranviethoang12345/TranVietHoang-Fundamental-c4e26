
from turtle import *

speed(0)

a = ['red','blue','brown','yellow','grey']
n= 3

for i in range (5):
    color (a[i])
    for m in range (n):
        forward(100)
        left(180-((n-2)*180)/n)
    n +=1

mainloop()