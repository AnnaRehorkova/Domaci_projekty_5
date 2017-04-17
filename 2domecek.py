from turtle import forward, left, right, exitonclick
from math import degrees, atan, sqrt, asin#asin zjistí úhel, samotný sin vyjadřuje jen poměr stran

def domecek(a, b):

    forward(a)
    left(90)
    forward(b)
    left(180-degrees(atan(a/b)))
    forward(sqrt(a**2 + b**2))
    left(90 + degrees(atan(a/b)))
    forward(a)
    left(180-degrees(atan(b/a)))
    forward(sqrt(a**2 + b**2))
    left(90 + degrees(atan(b/a)))
    forward(b)
    left(180)
    forward(b)
    right(90)
    forward(a)
    left(180-degrees(atan(b/a)))
    forward((sqrt(a**2 + b**2)/2))
    left(180-degrees(2*(asin((a/2)/(sqrt(a**2 + b**2)/2)))))
    forward((sqrt(a**2 + b**2)/2))

    exitonclick()

domecek(100, 100)
