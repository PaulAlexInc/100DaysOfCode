#Draw a square
from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

for i in range(4):
    tim.forward(100)
    tim.right(90)

screen.exitonclick()