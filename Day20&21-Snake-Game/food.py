from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # Normally the size is 20 by 20 pixels but to make it smaller i.e. 10 by 10 we need to stretch it by 0.5
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest") #So that animation of the food being created and its movent is not seen.
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 27)
        self.goto(random_x, random_y)
