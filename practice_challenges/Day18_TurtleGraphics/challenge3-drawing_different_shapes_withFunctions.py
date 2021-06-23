from turtle import Turtle, Screen
import random
colors = ["purple","indian red","medium aquamarine","cornflower blue","crimson","navy","lawn green","red", "orange red", "medium slate blue", "teal"]
tim = Turtle()
screen = Screen()

def draw_shape(num_sides):
    angle = 360/num_sides
    tim.pencolor(random.choice(colors))
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
for i in range (3,11):
    draw_shape(i)
screen.exitonclick()