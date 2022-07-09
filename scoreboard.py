from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.level = 0
        with open('data.txt') as high_score:
            self.high_level = int(high_score.read())
        self.goto(-250, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Level: {self.level} High score: {self.high_level}' , align='left', font=FONT)

    def add_point(self):
        self.level += 1
        self.update_scoreboard()

    def reset(self):
        if self.level > self.high_level:
            self.high_level = self.level
            with open('data.txt', mode='w') as high_score:
                high_score.write(str(self.level))
        self.level = 0
        self.update_scoreboard()
