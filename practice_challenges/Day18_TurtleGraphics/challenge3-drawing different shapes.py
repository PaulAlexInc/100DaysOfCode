#Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
from turtle import Turtle, Screen
import random
colors = ["blue","black","brown","red","yellow","green","orange","turquoise","pink"]
tim = Turtle()
screen = Screen()
n=3#n is the number of sides
while n<=10:
    color = random.choice(colors)
    tim.pencolor(color)
    for _ in range(n):
        tim.forward(100)
        tim.right(360/n)
    n+=1
screen.exitonclick()

