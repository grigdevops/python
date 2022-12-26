from turtle import Turtle
ALIGNEMENT = "center"
FONT = ("Arial",  24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,750)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNEMENT, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNEMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()




