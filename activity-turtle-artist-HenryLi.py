# Turtle Artist
# Author: Henry Li
# Date: 2025-10-28

import turtle

# A one of a kind drawing
wn = turtle.Screen()
t = turtle.Turtle()


# Set background
wn.bgcolor("skyblue")
t.color("white")
t.shape("turtle")
t.speed("fastest")
t.turtlesize(0.5)
t.pencolor("black")
t.pensize(3)
t.penup()
t.goto(0, 0)
t.left(90)


# Draw  the bottom left window
def draw_topleft_window(length: float):
    if length < 5:
        t.penup()
        t.showturtle()
        t.goto(0, 0)
        t.right(180)

    else:

        def rightL():
            t.forward(length / 2)
            t.right(90)
            t.forward(length)
            t.left(90)
            t.forward(length / 2)

        def leftL():
            t.forward(length / 2)
            t.left(90)
            t.forward(length)
            t.right(90)
            t.forward(length / 2)

        t.hideturtle()
        t.pendown()
        for _ in range(4):
            t.forward(length)
            t.left(90)
        leftL()
        t.right(90)
        rightL()
        t.left(90)
        draw_topleft_window(length // 2)


def draw_bottomleft_window(length: float):
    if length < 5:
        t.penup()
        t.showturtle()
        t.goto(0, 0)

    else:

        def rightL():
            t.forward(length / 2)
            t.right(90)
            t.forward(length)
            t.left(90)
            t.forward(length / 2)

        def leftL():
            t.forward(length / 2)
            t.left(90)
            t.forward(length)
            t.right(90)
            t.forward(length / 2)

        t.hideturtle()
        t.pendown()
        for _ in range(4):
            t.forward(length)
            t.right(90)
        rightL()
        t.left(90)
        leftL()
        t.right(90)
        draw_bottomleft_window(length // 2)


def draw_bottomright_window(length: float):
    if length < 5:
        t.penup()
        t.showturtle()
        t.goto(0, 0)
        t.left(180)

    else:

        def rightL():
            t.forward(length / 2)
            t.right(90)
            t.forward(length)
            t.left(90)
            t.forward(length / 2)

        def leftL():
            t.forward(length / 2)
            t.left(90)
            t.forward(length)
            t.right(90)
            t.forward(length / 2)

        t.hideturtle()
        t.pendown()
        for _ in range(4):
            t.forward(length)
            t.left(90)
        leftL()
        t.right(90)
        rightL()
        t.left(90)
        draw_bottomright_window(length // 2)


def draw_topright_window(length: float):
    if length < 5:
        t.penup()
        t.showturtle()

    else:

        def rightL():
            t.forward(length / 2)
            t.right(90)
            t.forward(length)
            t.left(90)
            t.forward(length / 2)

        def leftL():
            t.forward(length / 2)
            t.left(90)
            t.forward(length)
            t.right(90)
            t.forward(length / 2)

        t.hideturtle()
        t.pendown()
        for _ in range(4):
            t.forward(length)
            t.right(90)
        rightL()
        t.left(90)
        leftL()
        t.right(90)
        draw_topright_window(length // 2)


draw_topleft_window(400)
draw_bottomleft_window(400)
draw_bottomright_window(400)
draw_topright_window(400)


wn.exitonclick()
