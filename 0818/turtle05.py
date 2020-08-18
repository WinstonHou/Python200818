import turtle
a=int(input("enter a number:"))
for i in range(a):
    turtle.forward(50)
    turtle.right(360/a)
turtle.done()
