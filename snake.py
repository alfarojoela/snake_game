from turtle import Turtle, Screen
#solution differs in that it is used as constant rather than a class attribute
STARTING_POSITIONS = [
    (0, 0), (-20, 0), (-40, 0)
]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
  #      self.starting_positions = [
  #          (0, 0), (-20, 0), (-40, 0)
  #      ]

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)

    def snake_movement(self):
        # arguments for range function: start, stop, step
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # this is the last segment

        self.segments[0].forward(MOVE_DISTANCE)

'''
ABOVE loop took a while to understand.  
range starts at back of list.
stops just before 0 subscript.
steps back -1.
in base case with just 3 segments:

1st iteration:
new_x is assigned pointB's x
new_y is assigned pointB's y
point C is then assigned B's x and y coordinates.

2nd iteration:
new_x is assigned pointA's x
new_y is assigned pointA's y
point B is then assigned A's x and y coordinates.

NO 3RD ITERATION:
stops just before reaching 0.

outside of the loop, the head of the snake at segments[0] is moved forward 20 steps.

if the snake continues to grow the last segment is iterated all the way to the segment right before the head.
in EVERY case.
segments = [pointA, pointB, pointC]
'''

