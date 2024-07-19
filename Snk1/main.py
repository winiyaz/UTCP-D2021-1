# D20 -

from turtle import Turtle, Screen

scn = Screen()
scn.setup(width=600, height=600)
scn.bgcolor("#020617")
scn.title("PussyJuices")

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
	for s in segs:
		s.forward(20)






# ---
scn.exitonclick() # Exit on clic
# ---
