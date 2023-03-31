from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.up()
        self.shapesize(stretch_wid=1, stretch_len=5, outline=0)
        self.goto(0, -250)

    def move_left(self):
        if self.xcor() < -350:
            new_x = self.xcor() - 0
            self.goto(new_x, self.ycor())
        else:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() > 350:
            new_x = self.xcor() + 0
            self.goto(new_x, self.ycor())
        else:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())

