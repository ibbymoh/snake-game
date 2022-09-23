from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen = Screen()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
snake_segments = []
game_is_on = True
screen.tracer(0)

new_score = 0
while game_is_on:
    if snake.snake_segments[0].distance(food.pos()) < 12:
        food.refresh()
        scoreboard.update_score()
        snake.extend()
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with wall
    if snake.snake_segments[0].xcor() >280 or snake.snake_segments[0].xcor() < -280 or snake.snake_segments[0].ycor() > 280 or snake.snake_segments[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


    for i in range (3,len(snake.snake_segments)-1):
        #can also use for snake in snake.snake_segments[2:5] via splicing
        if snake.snake_segments[0].distance(snake.snake_segments[i].position()) < 20:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()

