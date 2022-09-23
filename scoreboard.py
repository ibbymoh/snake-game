import turtle
from turtle import Turtle

class Scoreboard(Turtle):
    #The variables that the class is initialised with. The self is taken as an argument in the functions in case there is
    #a desire to change anything.
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.pencolor('white')
        self.write("Score: " + str(self.score) ,move=True, align='center', font=('Arial', 13, 'normal'))
        self.color('black')

    def game_over(self):
        self.goto(0,0)
        self.color('white')
        self.write("Game Over" ,move=True, align='center', font=('Arial', 15, 'normal'))

        self.write
    def update_score(self):
        self.clear()
        self.score += 1
        self.goto(0, 280)
        self.pencolor('white')
        self.write("Score: " + str(self.score), move=True, align='center', font=('Arial', 13, 'normal'))
        self.color('black')


