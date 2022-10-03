from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.speed("fastest")
        self.penup()
        self.goto(0, 250)
        self.pendown()
        self.score = 0
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Arial', 30, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()




