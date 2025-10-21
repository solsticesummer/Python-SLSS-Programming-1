# recursion
# Author: Henry
# Date: 20 Oct 2025

# We're drawing trees (recursivey)
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

t = turtle.Turtle()

t.left(90)
t.color("brown")
t.pensize(5)
t.shape("turtle")
t.penup()
t.goto(0, -100)
t.pendown()


def draw_tree(level: int, branch_length: float):
    # Base case: if level is 0, draw a single branch
    if level == 0:
        t.color("blue")
        t.stamp()
        t.color("brown")
        return

    # Recursive case: draw a branch and two smaller trees
    else:
        t.forward(branch_length)
        t.right(30)
        draw_tree(level - 1, branch_length * 0.8)
        t.left(60)
        draw_tree(level - 1, branch_length * 0.8)
        t.right(30)
        t.backward(branch_length)


draw_tree(6, 120)

wn.exitonclick()


# import turtle

# wn = turtle.Screen()
# wn.bgcolor("skyblue")

# t = turtle.Turtle()
# t.shape("turtle")
# t.goto(0, -100)
# t.left(90)
# t.speed("fastest")
# t.pensize(5)


# def draw_complicatedtree(level: int, branch_length: float):
#     # Base case: if level is 0, draw a single branch
#     if level == 0:
#         t.color("green")
#         t.stamp()
#         t.color("brown")
#         return
#     # Recursive case: draw a branch and two smaller trees
#     else:
#         t.forward(branch_length)
#         t.right(40)
#         draw_complicatedtree(level - 1, branch_length / 1.618)
#         t.left(40)
#         draw_complicatedtree(level - 1, branch_length / 1.618)
#         t.left(40)
#         draw_complicatedtree(level - 1, branch_length / 1.618)
#         t.right(40)
#         t.backward(branch_length)


# draw_complicatedtree(5, 120)

# wn.exitonclick()
