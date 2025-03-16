from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier',12, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.sety(280)
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align='center', font=('Courier', 18, 'bold'))