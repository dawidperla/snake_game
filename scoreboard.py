from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            result = file.read()
        self.heigh_score = result
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(self.write(f"Score: {self.score},  Heighest score: {self.heigh_score}", align="center", font=("Arial", 24, "normal")))

    def reset_sc(self):

        if self.score > int(self.heigh_score):
            self.heigh_score = self.score
            with open("data.txt", mode = "w") as file:
                file.write(str(self.heigh_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align="center", font=("Arial", 24, "normal"))





    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}, Heighest score: {self.heigh_score} ", False, align="center", font=("Arial", 24, "normal"))