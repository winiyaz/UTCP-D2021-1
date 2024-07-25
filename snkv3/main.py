# This is the second version of the code , being made here for further work

import time
from turtle import Screen

from snake import Snake

scn = Screen()
scn.setup(width=600, height=600)
scn.bgcolor("#020617")
scn.title("PussyJuices")
scn.tracer(0)

snake = Snake()

scn.listen()
scn.onkey(snake.up, "Up")
scn.onkey(snake.down, "Down")
scn.onkey(snake.left, "Left")
scn.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
	scn.update()
	time.sleep(0.1)
	snake.move()

# ---
scn.exitonclick()  # Exit on clic
# ---
