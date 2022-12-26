import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
timmy = Turtle()
timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()


color_list = [(198, 12, 198), (250, 237, 250), (39, 76, 39), (38, 217, 38), (238, 227, 238), (229, 159, 229), (27, 40, 27), (215, 74, 215), (15, 154, 15), (199, 14, 199), (242, 246, 242), (243, 33, 243), (229, 17, 229), (73, 9, 73), (60, 14, 60), (224, 141, 224), (10, 97, 10), (221, 160, 221), (17, 18, 17), (46, 214, 46), (11, 227, 11), (81, 73, 81), (238, 156, 238), (74, 213, 74), (77, 234, 77), (52, 234, 52), (3, 67, 3)]


timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:

        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)



screen = Screen()
screen.exitonclick()




# import colorgram
#
#
# rgb_colors = []
# colors = colorgram.extract('img.png', 30)
#
# print(colors)
#
#
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.r
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)