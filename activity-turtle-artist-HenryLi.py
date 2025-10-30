# Turtle Artist
# Author: Henry Li
# Date: 2025-10-28

import turtle

# A one of a kind drawing
wn = turtle.Screen()
t = turtle.Turtle()


# Set background and turtle
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


# Draw the top left window
def draw_topleft_window(length: float):
    # The recursion stops when length is less than 5
    if length < 5:
        t.penup()
        t.showturtle()
        t.goto(0, 0)
        t.right(180)

    else:
        # rightL function to draw a right L shape
        def rightL():
            t.forward(length / 2)
            t.right(90)
            t.forward(length)
            t.left(90)
            t.forward(length / 2)

        # leftL function to draw a left L shape
        def leftL():
            t.forward(length / 2)
            t.left(90)
            t.forward(length)
            t.right(90)
            t.forward(length / 2)

        # start drawing
        t.hideturtle()
        t.pendown()
        # draw the outline for the new window
        for _ in range(4):
            t.forward(length)
            t.left(90)
        # draw the cross in the new window
        leftL()
        t.right(90)
        rightL()
        t.left(90)
        # Recursion to draw the next smaller window
        draw_topleft_window(length // 2)


# Draw the bottom left window
def draw_bottomleft_window(length: float):
    # The recursion stops when length is less than 5
    if length < 5:
        t.penup()
        t.showturtle()
        t.goto(0, 0)

    else:
        # rightL function to draw a right L shape
        def rightL():
            t.forward(length / 2)
            t.right(90)
            t.forward(length)
            t.left(90)
            t.forward(length / 2)

        # leftL function to draw a left L shape
        def leftL():
            t.forward(length / 2)
            t.left(90)
            t.forward(length)
            t.right(90)
            t.forward(length / 2)

        # start drawing
        t.hideturtle()
        t.pendown()
        # draw the outline of the new window
        for _ in range(4):
            t.forward(length)
            t.right(90)
        # draw the cross in the new window
        rightL()
        t.left(90)
        leftL()
        t.right(90)
        # Recursion to draw the next smaller window
        draw_bottomleft_window(length // 2)


# Draw the bottom right window
def draw_bottomright_window(length: float):
    # The recursion stops when length is less than 5
    if length < 5:
        t.penup()
        t.showturtle()
        t.goto(0, 0)
        t.left(180)

    else:
        # rightL function to draw a right L shape
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

        # start drawing
        t.hideturtle()
        t.pendown()
        # draw the outline of the new window
        for _ in range(4):
            t.forward(length)
            t.left(90)
        # draw the cross in the new window
        leftL()
        t.right(90)
        rightL()
        t.left(90)
        # Recursion to draw the next smaller window
        draw_bottomright_window(length // 2)


# Draw the topright window
def draw_topright_window(length: float):
    # The recursion stops when length is less than 5
    if length < 5:
        t.penup()
        t.showturtle()

    else:
        # rightL function to draw a right L shape
        def rightL():
            t.forward(length / 2)
            t.right(90)
            t.forward(length)
            t.left(90)
            t.forward(length / 2)

        # leftL function to draw a left L shape
        def leftL():
            t.forward(length / 2)
            t.left(90)
            t.forward(length)
            t.right(90)
            t.forward(length / 2)

        # start drawing
        t.hideturtle()
        t.pendown()
        # draw the outline of the new window
        for _ in range(4):
            t.forward(length)
            t.right(90)
        # draw the cross in the new window
        rightL()
        t.left(90)
        leftL()
        t.right(90)
        # Recursion to draw the next smaller window
        draw_topright_window(length // 2)


# run the functions
draw_topleft_window(400)
draw_bottomleft_window(400)
draw_bottomright_window(400)
draw_topright_window(400)

# exit the window
wn.exitonclick()
