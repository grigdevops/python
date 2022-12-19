from turtle import Turtle, Screen
import random
timm = Turtle()

timm.shape("turtle")
timm.color("red")
# timmy_the_turtle.forward(300)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(300)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(300)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(300)



# def triangle():
#     for _ in range(3):
#         timm.forward(100)
#         timm.left(120)
#
# def square():
#     for _ in range(4):
#         timm.forward(100)
#         timm.left(90)


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SeaGreen"]

def broctagon(n):
    for _ in range(n):
        timm.forward(100)
        timm.left(360/n)


for i in range(3, 10):
    timm.color(random.choice(colours))
    broctagon(i)



# triangle()
# square()
# broctagon(5)
# broctagon(6)
# broctagon(7)
# broctagon(8)





# for i in range(5,9):
#     broctagon(i)



screen = Screen()
screen.exitonclick()