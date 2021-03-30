from turtle import *
from itertools import count

COLOR = ["purple", "green", "orange", "blue", "red"]

def donut(d):
    for i in range(360):
        pencolor(COLOR[i % len(COLOR)])
        forward(d)
        left(121)

def star():
    for i in count():
        pencolor(COLOR[i % len(COLOR)])
        forward(i)
        right(144)

def shape(n):
    for i in range(n):
        forward(50)
        right(360 / n)

def main():
    donut(50)
    donut(100)

if __name__ == "__main__":
    speed(0)
    main()
    exitonclick()
