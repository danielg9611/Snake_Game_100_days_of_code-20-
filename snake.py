from turtle import Turtle

class Snake:
    segments = []
    STARTING_POSITIONS=[(0, 0), (-10, 0), (-20, 0)]
    MOVE_DISTANCE = 10

    def __init__(self):
        for position in self.STARTING_POSITIONS:
            new_segment = Turtle(shape='square')
            new_segment.color('dark gray','silver')
            new_segment.shapesize(.5, .5)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        self.head = self.segments[0]

    def length(self):
        return len(self.head)

    def move(self):
        for n in range(len(self.segments) - 1, 0, -1):
            self.segments[n].goto(self.segments[n - 1].position())
        self.head.fd(self.MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def grow(self):
        new_segment = Turtle(shape='square')
        new_segment.color('dark gray','silver')
        new_segment.shapesize(.5, .5)
        new_segment.penup()
        new_segment.speed('slow')
        self.segments.append(new_segment)

    def self_collision(self):
        for n in range(1,len(self.segments)):
            if self.head.distance(self.segments[n]) <5:
                return True
        return False