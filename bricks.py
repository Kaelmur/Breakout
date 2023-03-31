from turtle import Turtle


class Bricks:
    def __init__(self):
        self.all_bricks = []
        self.create_brick()

    def create_brick(self):
        x_pos = range(-355, 365, 70)
        y_pos = [160, 130, 100]
        for m in range(3):
            for i in range(11):
                j = Turtle()
                j.color("white")
                j.shape("square")
                j.up()
                j.shapesize(stretch_wid=1, stretch_len=3, outline=0)
                j.goto(x_pos[i], y_pos[m])
                self.all_bricks.append(j)
