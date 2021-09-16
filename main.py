from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions =[(0,0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
                            #arguments for range function: start, stop, step
    for seg_num in range(len(segments) -1, 0, -1 ):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)  #this is the last segment
    segments[0].forward(20)







screen.exitonclick()
###################MY CODE#####################################
# def turtle_attributes(turtle, x_coord, y_coord):
#     turtle.color("white")
#     turtle.shape("square")
#     turtle.setposition(x_coord, y_coord)
#
#
# # def turtle_attribute_creation():
# #     new_turtle = Turtle()
# #     new_turtle.color("orange")
# #     new_turtle.setposition(-50, 50)
# #     return new_turtle
#
#
# segment1 = Turtle()
# segment2 = Turtle()
# segment3 = Turtle()
#
# turtle_attributes(segment1, 0, 0)
# turtle_attributes(segment2, -20, 0)
# turtle_attributes(segment3, -40, 0)
#
#
###########################################################################################

