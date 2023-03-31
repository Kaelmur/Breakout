from turtle import Turtle

FONT = ('Distant Galaxy', 24, 'normal')


class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.hideturtle()
        self.lives = 3
        self.goto(0, 260)
        self.write(arg=f"Life: {self.lives}", align="center", font=FONT)

    def update(self):
        self.goto(0, 260)
        self.write(arg=f"Life: {self.lives}", align="center", font=FONT)

    def death(self):
        self.lives -= 1
        self.clear()
        self.update()
