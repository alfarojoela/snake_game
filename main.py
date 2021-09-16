from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  #new positions need continual refresh of screen
    time.sleep(0.1) #DELAYS REFRESH without it, just a quick blur
    snake.snake_movement()








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

