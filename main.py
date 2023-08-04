from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)


paddle = Paddle()
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(paddle.left_move_up, 'w')
screen.onkeypress(paddle.left_move_down, 's')
screen.onkeypress(paddle.right_move_down, 'Down')
screen.onkeypress(paddle.right_move_up, 'Up')

while 1:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # bouncing ball on walls
    if ball.ycor() > 270 or ball.ycor() <-270:
        ball.bounce_y() 
    # bouncing ball on right paddle
    if ball.distance(paddle.paddle[0])<50 and ball.xcor()>320:
        ball.bounce_x() 
    # bouncing ball on left paddle
    if ball.distance(paddle.paddle[1])<50 and ball.xcor()<-320:
        ball.bounce_x() 
        
    if ball.xcor()>380:
        score.l_score()
        ball.pos_reset()
    
    if ball.xcor()<-380:
        score.r_score()
        ball.pos_reset()
    



screen.exitonclick()