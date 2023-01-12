from turtle import Screen, Turtle
from paddle import Paddle
import  time
from scoreboard import Scoreboard
from ball import Ball




screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

new_paddle_r = Paddle((350, 0))
new_paddle_l = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(new_paddle_r.go_up, "Up")
screen.onkey(new_paddle_r.go_down, "Down")
screen.onkey(new_paddle_l.go_up, "w")
screen.onkey(new_paddle_l.go_down, "s")



game_is_on  = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(new_paddle_r) < 50 and ball.xcor() > 320 or ball.distance(new_paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()









screen.exitonclick()