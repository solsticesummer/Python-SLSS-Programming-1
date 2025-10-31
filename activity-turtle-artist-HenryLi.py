# Turtle Artist
# Author: Henry Li
# Date: 2025-10-28

import turtle
import random

# A one of a kind drawing

# Set up window
wn = turtle.Screen()
# Set up turtle
t = turtle.Turtle()

# Dictionary of colors for different sized windows
window_colors = {
    1: "#FF0000",
    2: "#6A0D83",
    3: "#9400D3",
    4: "#0000FF",
    5: "#00FF00",
    6: "#FF00FF",
    7: "#FF7F50",
    8: "#FF00FF",
    9: "#EEAF61",
    10: "#065535",
    11: "#B0BF1A",
    12: "#0070FF",
}

# Set background color
wn.bgcolor("skyblue")
# Set color
t.color("white")
# Set shape
t.shape("turtle")
# Set drawing speed
t.speed("fastest")
# Set turtle size
t.turtlesize(0.5)
# Set the drawing's color
t.pencolor("black")
# Set the drawing's size
t.pensize(3)
t.penup()
# go back to origin in the right direction
t.goto(0, 0)
t.left(90)


# Draw the top left window
def draw_topleft_window(length: float):
    # The recursion stops when length is less than 5
    if length < 5:
        # stop drawing
        t.penup()
        t.showturtle()
        # go back to origin in the right direction
        t.goto(0, 0)
        t.right(180)
        return

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

        t.begin_fill()
        t.color(window_colors[random.randint(1, 12)])
        # draw the outline for the new window
        for _ in range(4):
            t.forward(length)
            t.left(90)
        t.end_fill()
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
        # Stop drawing
        t.penup()
        t.showturtle()
        # Go back to origin
        t.goto(0, 0)
        return

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
        # Start filling
        t.begin_fill()
        # Pick a random color
        t.color(window_colors[random.randint(1, 12)])
        # draw the outline of the new window
        for _ in range(4):
            t.forward(length)
            t.right(90)
        # End fill
        t.end_fill()
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
        # Stop drawing
        t.penup()
        t.showturtle()
        # Go back to origin
        t.goto(0, 0)
        t.left(180)
        return

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
        # Start Fill
        t.begin_fill()
        # Pick random window color
        t.color(window_colors[random.randint(1, 12)])
        # draw the outline of the new window
        for _ in range(4):
            t.forward(length)
            t.left(90)
        # End fill
        t.end_fill()
        # draw the cross in the new window
        leftL()
        t.right(90)
        rightL()
        t.left(90)
        # Recursion to draw the window again with half the length
        draw_bottomright_window(length // 2)


# Draw the topright window
def draw_topright_window(length: float):
    # The recursion stops when length is less than 5
    if length < 5:
        # stop drawing
        t.penup()
        t.showturtle()
        return

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
        # Start fill
        t.begin_fill()
        # Pick random window color
        t.color(window_colors[random.randint(1, 12)])
        # draw the outline of the new window
        for _ in range(4):
            t.forward(length)
            t.right(90)
        # End fill
        t.end_fill()
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
