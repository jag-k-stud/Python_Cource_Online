from turtle import *

COLOR = ["red", "blue", "pink", "orange", "green"]

def ninja():
    for i in range(180):
        pencolor(COLOR[i % len(COLOR)])
        forward(100)
        right(30)
        forward(20)
        left(60)
        forward(50)
        right(30)

        penup()
        setposition(0, 0)
        pendown()
        right(2)

def star():
    for i in range(50):
        pencolor(COLOR[i % len(COLOR)])

        forward(i * 10)
        right(144)

def circres():
    pencolor("blue")
    for i in range(50):
        pencolor(COLOR[i % len(COLOR)])
        forward(50)
        right(123)

    pencolor("red")
    for i in range(1000):
        pencolor(COLOR[i % len(COLOR)])
        forward(100)
        right(121)

def shape(n):
    for i in range(n):
        forward(1)
        right(360 / n)

def main():
    ninja()


if __name__ == "__main__":
    speed(0)
    main()
    exitonclick()
