import turtle
import time
a=turtle.Turtle()
b=turtle.Turtle()
a.color("blue")
b.color("yellow")
a.pensize("10")
b.pensize("5")
for i in range(360):
    a.forward(1)
    a.left(1)
    b.forward(1)
    b.right(1)