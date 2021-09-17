from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)   #needs to be positioned before write function
        self.color("white")  # needs to have white color before write function.  otherwise will show up black against black bg
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def get_score(self):
        return self.score

