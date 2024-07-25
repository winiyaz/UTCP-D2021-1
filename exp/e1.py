# This will contain various experiments

# This is for writing text on the turtle graphics screen

import turtle

# Create a turtle screen and a turtle object
screen = turtle.Screen()
t = turtle.Turtle()

# Move the turtle to a specific position
t.penup()
t.goto(-100, 50)
t.pendown()

# Write text at the current turtle position
t.write("Hello, Turtle!", font=("Arial", 16, "normal"))

# Hide the turtle and keep the screen open
# t.hideturtle()
turtle.done()
