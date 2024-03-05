#Gregory Jepsen
#Turtle house
import turtle
t=turtle.Turtle()
t.shape('turtle')
t.speed(0)
colors=['violet','indigo','blue','green','yellow','orange','red']
def move(dis):
    t.penup()
    t.fd(dis)
    t.pendown()
    t.setheading(0)
def movet(righ, up2):
    right(righ)
    up(up2)
def up(dis):
    t.setheading(90)
    move(dis)

def down(dis):
    up(-1*dis)

def right(dis):
    t.setheading(0)
    move(dis)

def left(dis):
    right(-1*dis)
def square(size):
    for i in range(4):
        t.fd(size)
        t.rt(90)
def arc(size):
    t.setheading(90)
    for i in range(90):
        t.fd(.6*size)
        t.rt(180/90)
def rec(length, width):
    for i in range(2):
        t.fd(length)
        t.rt(90)
        t.fd(width)
        t.rt(90)
def octagon(size):
    for i in range(8):
        t.fd(size)
        t.lt(45)

def stop(size):
    t.setheading(0)
    octagon(size)
    move(3/8*size)
    rec(1/5*size,size*2)
def rainbow(cloud="none"):
    t.width(20)
    colorIndex=0
    cloudColor = 'light gray'
    for c in range(len(colors)):
        pos=t.position()
        print(pos)
        t.color(colors[colorIndex])
        arc(c+1)
        if cloud != 'none':
            if c==0:
                mark(30,cloudColor)
            elif c== 1 or c==5:
                mark(45,cloudColor)
            elif c== 2 or c==4:
                mark(30,cloudColor)
            elif c== 6:
                mark(45,cloudColor)
                right(10)
                mark(35,cloudColor)
                left(10)
            else:
                mark(70,cloudColor)
            t.penup()
        pos2 = t.position()
        print(pos2)
        colorIndex+=1
        t.goto(pos)
        if cloud != 'none':
            if c == 0:
                mark(30, cloudColor)
            elif c == 1 or c == 5:
                mark(45, cloudColor)
            elif c == 2 or c == 4:
                mark(30, cloudColor)
            elif c==6:
                mark(40,cloudColor)
                left(10)
                mark(35,cloudColor)
                right(10)
            else:
                mark(70, cloudColor)
        left(17)
    right(136)
    t.setheading(90)
    t.color('green')

def tri(size):
    for i in range(3):
        t.fd(size)
        t.lt(120)
def win(size):
    square(size)
    down(1/2*size)
    t.fd(size)
    movet(-1/2*size,1/2*size)
    t.rt(90)
    t.fd(size)
def house(size):
    square(size)
    tri(size)
    movet(1 / 5 * size, -1 / 5 * size)
    win(1 / 5 * size)
def dance(rot):
    t.speed(5)
    t.rt(rot*360)
    t.setheading(90)

def spin(rot):
    dance(-rot)

def star(size):
    t.color('yellow')
    for i in range(5):
        t.fd(size)
        t.rt(144)

def mark(size=50,color='white'):
    penSize=t.width()
    t.pendown()
    t.color(color)
    t.width(size)
    t.fd(1)
    t.back(1)
    t.width(penSize)
def ret(rig,up,apply(function)):
    movet(rig,up)
    function
    movet(-rig,-up)








#mark(50,'red')
#left(50)
#mark(10,'blue')
#tri(50)
#up(50)
#square(50)
# t.width(900000)
# t.color('light blue')
# t.fd(1)
#
# t.width(10)
# t.color('brown')
# movet(50,-50)
t.width(3)
house(80)
ret(50,50,'window(50)')
# t.color('blue')
# movet(-150,200)
# dance(3)
# star(80)
# t.color('blue')
# movet(50,-350)
# spin(2)
#stop(20)
#movet(250,300)

#rainbow(3)

#t.color('white')
#house(100)
#right(75)
#down(35)
#dance(3)

#right(50)
#up(100)
#left(60)
#rainbow()
#down(80)
#left(40)


turtle.Screen().exitonclick()
