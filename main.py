from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()  #new positions need continual refresh of screen

    #scoreboard.write(f"Score: {scoreboard.get_score()}", align="center", font=("Arial", 8, "normal"))
    time.sleep(0.1) #DELAYS REFRESH without it, just a quick blur
    snake.snake_movement()


    #DETECTION OF FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #WHY DOES THIS WORK?
    #detect collision with the tail
    for segment in snake.segments[1:]:
       if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()




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

