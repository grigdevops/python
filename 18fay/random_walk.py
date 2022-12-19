import turtle
from turtle import Turtle, Screen
import random
timm = Turtle()

turtle.colormode(255)



timm.shape("turtle")
timm.color("red")
timm.pensize(20)
timm.speed("fastest")


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SeaGreen"]



def walk(n):
    angles = [0,90, 180, 270 ]
    for _ in range(n):
        tup = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
        timm.pencolor(tup)
        # timm.color(random.choice(colours))
        timm.forward(30)
        timm.left(random.choice(angles))


walk(2000)


screen = Screen()
screen.exitonclick()
