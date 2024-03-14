#Gregory Jepsen
#Turtle Drawings
import turtle

t=turtle.Turtle()
#turtle.shape("turtle") # optional
#turtle.speed(0) # optional

def move(size):
    t.penup()
    t.fd(size)
    t.pendown()

#Initiates lists
sides=[]
color=[]
size=[]
bold=[]

#User defined inputs
numShapes=int(input("How many shapes do you want? "))
for n in range(numShapes):
    print("Shape",str(n+1)+":")
    sides.append(input("# of Sides: "))
    size.append(input("Size: "))
    color.append(input("What color would you like? ").title())
    boldTemp=(input('Would you like your shape bold? Yes/No: ').title())
    if boldTemp == "Yes":#Sets the width of the line
        bold.append("5")
    else:
        bold.append("1")
#Verifies what is being sent to turtle
print("Sides:",sides)
print("Size:",size)
print("Color:",color)
print("Bold:",bold)

#Draws shape
for i in range(numShapes):
    t.color(color[i])
    t.width(float(bold[i]))
    for j in range(int(sides[i])):#Draws the shape
        t.fd(float(size[i]))
        t.rt(360/float(sides[i]))
    move(size[i])
def square(size):
    for i in range(4):
        t.fd(size)
        t.rt(90)

def rec(length,width):
    for i in range(2):
        t.fd(length)
        t.rt(90)
        t.fd(width)
        t.rt(90)
t.penup()
t.goto(-300,0)
t.pendown()
for i in range(3):
    square(25)
    move(45)
    rec(25,100)
    move(45)

turtle.Screen().exitonclick()