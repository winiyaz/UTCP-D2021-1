# Food rendering logic here

import random as rp
from turtle import Turtle


class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_len=0.5, stretch_wid=0.5)
		self.color("#FFFF80")
		self.speed("fastest")

		# Generating the random axis
		random_x = rp.randint(-540, 540)
		random_y = rp.randint(-540, 540)
		self.goto(random_x, random_y)
