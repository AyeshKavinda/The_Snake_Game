from turtle import Turtle
import random
from scoreboard import ScoreBoard

score = ScoreBoard

class Bomb(Turtle):

    # if score == 5:
        def __init__(self):
            super().__init__()
            self.shape("circle")
            self.penup()
            self.shapesize(stretch_len=0.5, stretch_wid=0.5)
            self.color("red")
            self.speed("fastest")
            self.refresh_bomb()

        def refresh_bomb(self):
            x_axis = random.randint(-280, 280)
            y_axis = random.randint(-280, 280)
            self.goto(x_axis, y_axis)