from snake import Snake
from food import Food
from turtle import Screen
from score_board import Score
import time

screen = Screen()
screen.setup(600,600)
screen.colormode(255)
screen.bgcolor(30,30,30)
screen.tracer(0)
screen.title('Snake Game')

snake = Snake()

food = Food()

score = Score()

screen.listen()
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')


def space_cheat():
    snake.grow()
    score.increase_score()

screen.onkey(space_cheat, 'space')



game_on = True
while game_on:
    snake.move()
    screen.update()


    if food.distance(snake.head) < 9:
        snake.grow()
        food.random_pos()
        score.increase_score()
    if snake.head.xcor()>290 or snake.head.xcor() <-290 or snake.head.ycor()>290 or snake.head.ycor() <-290:
        game_on = False

    if snake.self_collision():
        game_on = False

    time.sleep(.1)
    screen.update()


score.game_over()

screen.exitonclick()
