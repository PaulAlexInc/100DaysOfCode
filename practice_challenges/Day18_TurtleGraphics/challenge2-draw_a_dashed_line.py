from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
for _ in range(15):
    tim.forward(10)#line
    tim.penup()
    tim.forward(10)#blank
    tim.pendown()
screen.exitonclick()