from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win tha race ? ")

is_race_on = False


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
point = 0
for i in range(5):

    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + point)
    point += 40
    all_turtles.append(new_turtle)

print(all_turtles)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win the game color is {winning_color}")
            else:
                print(f"You lose the game, winning color is {winning_color}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()

