# Drawing and Loops
# Author: Henry Li
# Oct 14, 2025
import turtle

wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")

# TMNT - turtles
mikey = turtle.Turtle()

# mikey.turtlesize(2)
# mikey.color("orange")
# mikey.pencolor("blue")
# mikey.shape("turtle")
# mikey.pendown()
# mikey.speed(2)

# mikey.left(45)
# mikey.fillcolor("orange")
# mikey.begin_fill()
# for i in range(4):
#     mikey.forward(200)
#     mikey.right(90)
# mikey.end_fill()
# mikey.penup()
# mikey.left(135)
# mikey.speed(3)
# mikey.pendown()
# mikey.left(45)
# mikey.begin_fill()
# for i in range(4):
#     mikey.forward(400)
#     mikey.right(90)
# mikey.end_fill()
# mikey.penup()
# mikey.hideturtle()

# mikey.goto(400, 100)
# mikey.showturtle()
# mikey.fillcolor("light blue")
# mikey.pendown()
# mikey.begin_fill()
# mikey.circle(50)
# mikey.end_fill()
# mikey.penup()
# mikey.forward(80)
# mikey.left(45)
# mikey.forward(127)
# mikey.pendown()
# mikey.begin_fill()
# mikey.circle(100)
# mikey.end_fill()
# mikey.hideturtle()

for counter in range(10):
    counter = counter + 50
    mikey.setheading(0)
    mikey.color("brown")
    mikey.turtlesize(1)
    mikey.speed(2)

    mikey.pu()
    mikey.goto(-5 + counter, -30 + counter)
    mikey.pd()
    mikey.circle(30)
    mikey.pu()

    mikey.goto(-10 + counter, 10 + counter)
    mikey.stamp()
    mikey.goto(10 + counter, 10 + counter)
    mikey.stamp()
    mikey.goto(10 + counter, -10 + counter)
    mikey.stamp()
    mikey.goto(-10 + counter, -10 + counter)
    mikey.stamp()
    mikey.goto(0 + counter, 0 + counter)
    mikey.stamp()
    mikey.hideturtle()

wn.exitonclick()
