import turtle
import random

def drunken_forward():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()
def drunken_backward():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()
def drunken_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
def drunken_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()
def drunken_escape():
    turtle.reset()
    
turtle.shape('turtle')

turtle.onkey(drunken_forward, 'w')
turtle.onkey(drunken_left, 'a')
turtle.onkey(drunken_backward, 's')
turtle.onkey(drunken_right, 'd')
turtle.onkey(drunken_escape, "Escape")
turtle.listen()
