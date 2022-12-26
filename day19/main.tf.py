from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def couter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def start():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="f", fun=move_backward)
screen.onkey(key="a", fun=couter_clockwise)
screen.onkey(key="q", fun=clockwise)
screen.onkey(key="c", fun=start)

screen.exitonclick()
