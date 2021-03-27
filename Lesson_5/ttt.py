# Черепашка
from turtle import *

DISTANCE = 100


def draw(turtle: Turtle, sides=4):
    for i in range(sides):
        turtle.forward(DISTANCE)
        turtle.right(360 / sides)


# def main(turtle: Turtle):
#     turtle.penup()
#     turtle.goto(-DISTANCE/2, DISTANCE*2)
#     turtle.pendown()
#     # deg = 45
#     # for _ in range(360 // deg):
#     #     turtle.left(deg)
#     for i in range(3, 15):
#         draw(turtle, i)

# def main(turtle: Turtle):
#     turtle.penup()
#     turtle.goto(-DISTANCE, DISTANCE)
#     turtle.pendown()
#     for i in range(1, 50):
#         turtle.forward(10 * i)
#         turtle.right(144)

# def main(turtle: Turtle):
#     turtle.pencolor('blue')

#     for i in range(360):
#         turtle.forward(50)
#         turtle.left(121)

#     turtle.pencolor('red')

#     for i in range(360):
#         turtle.forward(100)
#         turtle.left(121)


def main(turtle: Turtle):
    turtle.speed(0)

    for i in range(180):
        turtle.forward(100)
        turtle.right(30)
        turtle.forward(20)
        turtle.left(60)
        turtle.forward(50)
        turtle.right(30)

        turtle.penup()
        turtle.setposition(0, 0)
        turtle.pendown()
        turtle.right(2)

# Скинуть ссылку на TRON

if __name__ == "__main__":
    t = Turtle()
    main(t)
    exitonclick()
