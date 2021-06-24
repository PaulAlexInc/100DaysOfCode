# import colorgram
#
# colors = colorgram.extract('image.jpg',30)
# colorlist=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tup = (r,g,b)
#     colorlist.append(tup)
# print(colorlist)
import turtle as t
from turtle import Screen
import random
tim = t.Turtle()
t.colormode(255)#for rgb

color_list=[(58, 106, 148), (224, 200, 110), (134, 85, 59), (222, 139, 64), (195, 145, 171), (144, 179, 202), (139, 81, 104), (209, 91, 69), (68, 106, 90), (188, 80, 119), (135, 182, 137), (64, 156, 92), (47, 156, 193), (129, 134, 76), (183, 191, 201), (215, 177, 192), (20, 68, 114), (20, 59, 95), (174, 203, 181), (115, 123, 151), (229, 174, 165), (159, 205, 214), (70, 59, 48), (76, 63, 48), (121, 45, 57), (125, 44, 42)]
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
for _ in range(10):#vertical
    for _ in range(10):#horizontal
        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.forward(50)


    tim.left(90)
    tim.penup()
    tim.forward(50)
    tim.right(90)
    tim.backward(500)
screen = Screen()
screen.exitonclick()