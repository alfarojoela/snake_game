from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()  #call to super class.  Since Turtle is in parenthesis this is the super class.
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()  #calls refresh when food is consumed.  controlled in maim file

    #generates new random location for food object
    def refresh(self):
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)