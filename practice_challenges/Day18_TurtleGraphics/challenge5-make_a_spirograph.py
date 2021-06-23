import turtle as t
from turtle import Screen
import random
tim = t.Turtle()
t.colormode(255)#for rgb
screen = Screen()
tim.speed("fastest")

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tup=(r,g,b)
    return tup


def draw_spirograph(size_of_gap):
    for _ in range(360//size_of_gap):
        tim.color(random_color())
        tim.circle(radius)
        tim.setheading(tim.heading()+size_of_gap)
radius = 100
draw_spirograph(5)

#360//size_of_gap gives the total number of times the loop has to run exactly to make the spirograph without repeated overlaps
screen.exitonclick()