from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from bomb import Bomb
import time
# The Snake Game.

# 1. Create a snake body.
#
# 2. Move the snake.
#
# 3. Create snake food.
#
# 4. Detect collision with food.
#
# 5. Create a scoreboard.
#
# 6. Detect collision with wall.
#
# 7. Detect collision with tail.

##!------SCREEN SETUP AND CREATING THE SNAKE BODY------!##

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("Black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

snake = Snake()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

food = Food()

score = ScoreBoard()


##!------ANIMATING THE SNAKE SEGMENTS ON SCREEN------!##

game_on = True
while game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.reward_score()
        my_screen.update()

    # bomb_on = True
    # while bomb_on:
        bomb_on_teritory = True
        if score.score > 14:
            if score.score > 17:
                bomb_on_teritory = False
            elif bomb_on_teritory == True:
                bomb = Bomb()




    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    #Detect collision with tail.
    for block in snake.blocks[1:]:
        # if block == snake.head:
        #     pass
        if snake.head.distance(block) < 10:
            game_on = False
            score.game_over()

    #Denote bomb.
    # if score.score > 2:
    #     bomb = Bomb()
    #     for block in snake.blocks:
    #         if snake.head.distance(bomb) < 10:
    #             game_on = False
    #             score.game_over()

            # elif snake.blocks.distace(bomb) < 10:
            #     game_on = False
            #     score.game_over()



my_screen.exitonclick()