# Drawing and Loops
# Author: Henry Li
# Oct 14, 2025
import turtle

wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("lightgreen")

# TMNT - turtles
mikey = turtle.Turtle()
mikey.turtlesize(5)
mikey.color("orange")
mikey.pencolor("blue")
mikey.shape("turtle")
mikey.pendown()
mikey.speed(1)
mikey.left(45)
for i in range(4):
    mikey.forward(200)
    mikey.right(90)
mikey.penup()

wn.exitonclick()
