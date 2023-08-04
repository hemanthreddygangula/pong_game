from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update()
       
    
    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.left_score, align='center', font=('courier', 50, 'normal'))
        self.goto(100,200)
        self.write(self.right_score, align='center', font=('courier', 50, 'normal'))
    
    def l_score(self):
        self.left_score+=1
        self.update()
    
    def r_score(self):
        self.right_score+=1
        self.update()