# This is the second version of the code , being made here for further work

import time
from turtle import Turtle, Screen

scn = Screen()
scn.setup(width=600, height=600)
scn.bgcolor("#020617")
scn.title("PussyJuices")
scn.tracer(0)

sta_pos = [(0, 0), (-20, 0), (-40, 0)]  # Coordinate positions
segs = []

# Creating the diagram
for pos in sta_pos:
	new_seg = Turtle("square")
	new_seg.color("#db2777")
	new_seg.penup()
	new_seg.goto(pos)
	segs.append(new_seg)

game_is_on = True
while game_is_on:
	scn.update()
	time.sleep(0.1)

	for seg_num in range(len(segs) - 1, 0, -1):
		new_x = segs[seg_num - 1].xcor()
		new_y = segs[seg_num - 1].ycor()
		segs[seg_num].goto(new_x, new_y)
	segs[0].forward(20)
	segs[0].left(10)




# ---
scn.exitonclick()  # Exit on clic
# ---
