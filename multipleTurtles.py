import turtle
import random
# Method
#
# Parameter	Description	Example
# Turtle()	None	Creates and returns a new turtle object	tommy = turtle.Turtle()
# forward()	amount	Moves the turtle forward by the specified amount	tommy.forward(50)
# backward()	amount	Moves the turtle backward by the specified amount	tommy.backward(50)
# right()	angle	Turns the turtle clockwise	tommy.right(45)
# left()	angle	Turns the turtle counterclockwise	tommy.left(45)
# penup()	None	Picks up the turtle's Pen	tommy.penup()
# pendown()	None	Puts down the turtle's Pen	tommy.pendown()
# up()	None	Picks up the turtle's Pen	tommy.up()
# down()	None	Puts down the turtle's Pen	tommy.down()
# color()	Color name	Changes the color of the turtle's pen	tommy.color("blue")
# fillcolor()	Color name	Changes the color of the turtle will use to fill a polygon	tommy.fillcolor("green")
# heading()	None	Returns the current heading	print(tommy.heading())
# position()	None	Returns the current position	print(tommy.position())
# goto()	x, y	Move the turtle to position x,y	tommy.goto(-100, 25)
# begin_fill()	None	Remember the starting point for a filled polygon	tommy.begin_fill() ... tommy.end_fill()
# end_fill()	None	close the polygon and fill with the current fill color	tommy.begin_fill() tommy.end_fill()
# dot()	None	Leave a dot at the current position	tommy.dot()
# stamp()	None	Leaves an impression of a turtle shape at the current location	tommy.stamp()
# shape()	shapename	Should be 'arrow', 'classic', 'turtle', or 'circle'	tommy.shape("turtle")

t=turtle.turtle()
t.color('blue')
u=turtle.turtle()
u.color('blue')
r=turtle.turtle()
r.color('blue')

t.penup()
t.goto(-50,-50)
t.pendown()
t.color('black')
t.forward(100)
t.penup()


turtle.Screen().exitonclick()