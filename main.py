from turtle import Screen
from turtle import Turtle
from ball import Ball
from paddle import Paddle
from lives import Lives
from bricks import Bricks
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("BreakOut")
screen.tracer(0)
ball = Ball()
paddle = Paddle()
bricks = Bricks()
lives = Lives()
screen.listen()
screen.onkeypress(fun=paddle.move_left, key="Left")
screen.onkeypress(fun=paddle.move_right, key="Right")
game_is_on = True
score = 0
ball.goto(0, -210)

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.ycor() < -280:
        ball.goto(0, -210)
        lives.death()
        ball.move_speed = 0.1
        ball.bounce_y()

    for i in bricks.all_bricks:
        if i.distance(ball) < 40:
            i.hideturtle()
            i.goto(-1000, 1000)
            score += 100
            ball.bounce_y()
            ball.move_speed *= 0.95

    if score == 3300:
        you_won = Turtle()
        you_won.color("green")
        you_won.up()
        you_won.hideturtle()
        you_won.goto(0, 0)
        game_is_on = False
        you_won.write(arg="You win!", align="center", font=('Distant Galaxy', 24, 'normal'))
        time.sleep(1)
        print("You win! Restart app if you wanna play again!")

    if lives.lives == 0:
        game_is_on = False
        game_over = Turtle()
        game_over.color("red")
        game_over.up()
        game_over.hideturtle()
        game_over.goto(0, 0)
        game_over.write(arg="Game is over", align="center", font=('Distant Galaxy', 24, 'normal'))
        time.sleep(1)
        print("Game is over start app again!")
        exit()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.distance(paddle) < 31:
        ball.bounce_y()


screen.exitonclick()
