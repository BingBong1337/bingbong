import turtle as t
import random as r
aTurtle = t.Turtle()
bTurtle = t.Turtle()
cTurtle = t.Turtle()
dTurtle = t.Turtle()

def randomColor():
    R = r.random()
    G = r.random()
    B = r.random()
    aTurtle.color(R,G,B)
    bTurtle.color(R,G,B)

from turtle import*

speed(1000)
penup()
goto(-140, 220)

for step in range (16):
    write(step, align ='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

aTurtle.shape('turtle')
aTurtle.color('black')
aTurtle.shapesize(r.randint(1,100))
aTurtle.width(1)
aTurtle.speed(r.randint(0,100))

bTurtle.shape('turtle')
bTurtle.color('cyan')
bTurtle.shapesize(r.randint(1,100))
bTurtle.width(1)
bTurtle.speed(r.randint(0,100))

cTurtle.shape('turtle')
cTurtle.color('gray')
cTurtle.shapesize(r.randint(1,100))
cTurtle.width(1)
cTurtle.speed(r.randint(0,100))

dTurtle.shape('turtle')
dTurtle.color('lime')
dTurtle.shapesize(r.randint(1,100))
dTurtle.width(1)
dTurtle.speed(r.randint(0,100))

aTurtle.penup()
aTurtle.goto(-160,200)
aTurtle.pendown()

bTurtle.penup()
bTurtle.goto(-160,170)
bTurtle.pendown()


cTurtle.penup()
cTurtle.goto(-160,140)
cTurtle.pendown()

dTurtle.penup()
dTurtle.goto(-160,110)
dTurtle.pendown()
for i in range (10):
    aTurtle.right(36)
    bTurtle.left(36)
    cTurtle.right(36)
    dTurtle.left(36)
for i in range(100):
    aTurtle.forward(r.randint(1,5))

    bTurtle.forward(r.randint(1,5))

    cTurtle.forward(r.randint(1,5))

    dTurtle.forward(r.randint(1,5))











exitonclick()
