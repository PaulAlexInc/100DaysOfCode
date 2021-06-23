#random walk
import turtle as t
from turtle import Screen
import random
direction = [0,90,180,270]
tim = t.Turtle()

t.colormode(255)#for rgb

def  random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r,g,b)
    return tup


screen = Screen()
tim.pensize(15)
tim.speed("fastest")
while True:
    tim.pencolor(random_color())
    tim.forward(50)
    tim.setheading(random.choice(direction))

screen.exitonclick()

