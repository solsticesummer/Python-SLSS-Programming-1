# Drawing and Loops
# Author: Henry Li
# Oct 14, 2025
import turtle

wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")

# TMNT - turtles
mikey = turtle.Turtle()
mikey.turtlesize(2)
mikey.color("orange")
mikey.pencolor("blue")
mikey.shape("turtle")
mikey.pendown()
mikey.speed(2)
mikey.left(45)
for i in range(4):
    mikey.forward(200)
    mikey.right(90)
mikey.penup()
mikey.left(135)
mikey.speed(3)
mikey.pendown()
mikey.left(45)
for i in range(4):
    mikey.forward(400)
    mikey.right(90)
mikey.penup()
mikey.hideturtle()
mikey.goto(100, 100)
mikey.showturtle()
mikey.pendown()
mikey.begin_fill()
mikey.circle(50)
mikey.end_fill()
mikey.forward(80)
mikey.left(45)
mikey.penup()
mikey.forward(125)
mikey.pendown()
mikey.begin_fill()
mikey.circle(100)
mikey.end_fill()
mikey.hideturtle()

wn.exitonclick()
