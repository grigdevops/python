from turtle import Screen
from turtle import Turtle
from paddle import Paddle
import  time

from ball import Ball




screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
new_paddle_r = Paddle(350, 0)
new_paddle_l = Paddle(-350, 0)
ball = Ball()




screen.onkey(new_paddle_r.go_up, "Up")
screen.onkey(new_paddle_r.go_down, "Down")
screen.onkey(new_paddle_l.go_up, "w")
screen.onkey(new_paddle_l.go_down, "s")



game_is_on  = True

while game_is_on:
    time.sleep(0.01)
    screen.update()

    ball.move()






screen.exitonclick()