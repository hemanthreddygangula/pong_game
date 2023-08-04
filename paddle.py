from turtle import Turtle

class Paddle:
    def __init__(self):
        self.paddle = []
        self.paddle_right()
        self.paddle_left()

    def paddle_right(self):
        seg = Turtle('square')
        seg.color('white')
        seg.shapesize(stretch_wid=5, stretch_len=1)
        seg.penup()
        seg.goto(350, 0)
        self.paddle.append(seg)
    
    def paddle_left(self):
        seg = Turtle('square')
        seg.color('white')
        seg.shapesize(stretch_wid=5, stretch_len=1)
        seg.penup()
        seg.goto(-350, 0)
        self.paddle.append(seg)
    
    def right_move_up(self):
        new_y = self.paddle[0].ycor() + 40
        self.paddle[0].goto(self.paddle[0].xcor(), new_y)

    def left_move_up(self):
        new_y = self.paddle[1].ycor() + 40
        self.paddle[1].goto(self.paddle[1].xcor(), new_y)

    def right_move_down(self):
        new_y = self.paddle[0].ycor() - 40
        self.paddle[0].goto(self.paddle[0].xcor(), new_y)

    def left_move_down(self):
        new_y = self.paddle[1].ycor() - 40
        self.paddle[1].goto(self.paddle[1].xcor(), new_y)