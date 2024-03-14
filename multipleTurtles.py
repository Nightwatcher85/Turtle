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

t=turtle.Turtle()
t.color('red')
u=turtle.Turtle()
u.color('blue')
r=turtle.Turtle()
r.color('orange')
l=turtle.Turtle()
l.color('purple')

t.penup()
t.goto(-250,-155)
t.pendown()
t.color('light grey')
t.width(10)
t.forward(400)
t.color('red')
t.penup()

turtles=[t,u,r,l]

for tur in turtles:
    tur.penup()
    tur.goto(-200+(turtles.index(tur)*100),-150)
    tur.setheading(90)
    tur.pendown()
    tur.forward(200)

while

turtle.Screen().exitonclick()