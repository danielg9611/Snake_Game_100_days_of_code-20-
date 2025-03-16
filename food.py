import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.shapesize(.4,.4)
        self.penup()
        self.speed(0)
        self.random_pos()

    def random_pos(self):
        x_pos =random.choice(range(-280,281,10))
        y_pos = random.choice(range(-280, 281, 10))
        self.goto(x_pos,y_pos)
