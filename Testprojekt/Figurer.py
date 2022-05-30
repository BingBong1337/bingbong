import turtle as t


aTurtle = t.Turtle()
aTurtle.width(2)
aTurtle.speed()
aTurtle.forward(360)
aTurtle.right(90)
aTurtle.forward(180)
aTurtle.right(90)
aTurtle.forward(360)
aTurtle.right(90)
aTurtle.forward(180)

bTurtle=t.Turtle()
bTurtle.width(2)
bTurtle.speed()
bTurtle.penup()
bTurtle.goto(-200,100)
bTurtle.pendown()
bTurtle.fillcolor('red')
bTurtle.begin_fill()
bTurtle.left(60)
bTurtle.forward(60)
bTurtle.right(120)
bTurtle.forward(60)
bTurtle.right(120)
bTurtle.forward(60)
bTurtle.end_fill()

cTurtle=t.Turtle()
cTurtle.width(2)
cTurtle.speed()
cTurtle.penup()
cTurtle.goto(-200,-100)
cTurtle.pendown()
for i in range(3):
    cTurtle.left(120)
    cTurtle.forward(60)



eT=t.Turtle()
eT.width(1)
eT.speed(100)
eT.penup()
eT.goto(100,200)
eT.pendown()
eT.fillcolor('orange')
eT.begin_fill()
for i in range(100):
    eT.forward(1+i)
    eT.left(60)
eT.left(60)
eT.forward(100)
eT.end_fill()































t.exitonclick()
