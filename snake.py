from turtle import Turtle

POSITIONS = [(0,0),(0,-20),(0,-40)]

class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        snake = Turtle("square")
        snake.color("white")  # [0,-20,-40.] -> [20,0,]
        snake.penup()
        snake.goto(position)
        self.snake_segments.append(snake)



    def extend(self):
        self.add_segment(self.snake_segments[-1].position())




    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            # i want to set the coordinate of the last snake to the coordinate of the 2nd to last , and the 2nd  to the first
            old_position = self.snake_segments[i - 1].pos()
            self.snake_segments[i].setpos(old_position)


        self.snake_segments[0].forward(20)



    def up(self):
        if self.snake_segments[0].heading() != 270:
            self.snake_segments[0].setheading(90)


    def right(self):
        if self.snake_segments[0].heading() != 180:
            self.snake_segments[0].setheading(0)


    def left(self):
        if self.snake_segments[0].heading() != 0:
            self.snake_segments[0].setheading(180)


    def down(self):
        if self.snake_segments[0].heading() != 90:

            self.snake_segments[0].setheading(270)
