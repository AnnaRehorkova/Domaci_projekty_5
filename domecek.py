from turtle import forward, left, right, exitonclick
from math import sqrt

def domecek(a):
    for i in range(4):
        forward(a)
        left(90)

    left(45)
    forward(sqrt(2 * (a**2)))
    left(75)
    for i in range(2):
        forward(a)
        left(120)

    right(45)
    forward(sqrt(2 * (a**2)))
    left(45)
    forward(a)

    #exitonclick()

strana = (int(input("Zadej délku strany: ")))

domecek(strana)
domecek(strana*2) 
domecek(strana*3)

"""
for i in range(3):
    forward(a)
    left(120)

right(90)

for i in range(3):
    forward(a)
    left(90)

left(45)
forward(sqrt(2 * (a**2)))
right(135)
forward(a)
right(135)
forward(sqrt(2 * (a**2)))
left(45)
"""
