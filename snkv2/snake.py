# 188 - from snk1 organize code by pussystink
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Coordinate positions
MOVE_DISTANCE = 20


class Snake:
	"""Creates a snake with 3 squares and new starting positons"""

	def __init__(self):
		"""Create the snake which is squares from turtle"""
		self.segments = []
		self.create_snake()

	def create_snake(self):
		"""Setting the shape and color"""
		for pos in STARTING_POSITIONS:
			new_seg = Turtle("square")
			new_seg.color("#db2777")
			new_seg.penup()
			new_seg.goto(pos)
			self.segments.append(new_seg)

	def move(self):
		"""Moving the squares"""
		for seg_num in range(len(self.segments) - 1, 0, -1):
			new_x = self.segments[seg_num - 1].xcor()
			new_y = self.segments[seg_num - 1].ycor()
			self.segments[seg_num].goto(new_x, new_y)
		self.segments[0].forward(MOVE_DISTANCE)
