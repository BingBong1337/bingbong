import turtle as t
import numpy as np
from operator import add
FONTSIZE = 24



def calc_ellipse(t, origo):
    """
    Paramater: Ett tal och en tupel (koordinat)
    Returnerar: En koordinat
    Kommentar: Returkoordinaterna ligger på en ellips
    """
    # a och b styr storlek och form på ellipsen
    a = 100
    b = 50
    x = a*np.cos(t)
    y = b*np.sin(t)

    # Exempel på hur returen fungerar:
    # Om x = 100, y = 200 och origo = (30, -50)
    # så returneras (130, 150)
    return list(map(add, (x, y), origo))


def plot_ellipse(origo):
    """
    Parameter: En tupel (koordinat), som anger centrum för ellipsen
    Returnerar: Inget
    Kommentar: Proceduren ritar ellipsen, koordinater beräknas i
    funktionen calc_ellips
    """
    tim.color("Red")
    tim.penup()
    tim.goto(calc_ellipse(0, origo))  # Gå till första punkten på ellipsen
    tim.pendown()

    # Skapar en lista med tal mellan 0 och 2*pi med avståndet 0.025, dvs
    # 0, 0.025, 0.050, ... ,6.275
    t = np.arange(0, 2*np.pi, 0.025)

    for i in t:  # Ritar ellipsen
        tim.goto(calc_ellipse(i, origo))


def print_text(text, origo):
    """
    Parametrar: En text och en tupel (koordinat) som anger centrum för texten
    Returnerar: Inget
    Kommentar: Procedur som skriver ut texten i ellipsen
    """
    tim.penup()
    tim.color("white")
    tim.goto(origo[0], origo[1] - FONTSIZE/2)
    tim.write(text, font=("Arial", FONTSIZE, "normal"), align="center")
    
def calc_parabel(t,origo):
    a = 5
    x=a*t**2
    y=a*t
    return list(map(add,(x,y),origo))

def calc_parabel2(t,origo):
    a = 5
    x= a*t**2
    y= -a*t
    return list(map(add,(x,y),origo))

def calc_hyperbel(t,origo):
    a = 10
    b = 10
    x = a*np.cosh(t)
    y = b*np.sinh(t) 
    return list(map(add,(x,y),origo))

def calc_hyperbel2(t,origo):
     a = 10
     b = 10
     x = a*np.cosh(t)
     y = -b*np.sinh(t) 
     return list(map(add,(x,y),origo))
 
def calc_leminskata(t,origo):
    a = 100
    x = (a*np.cos(t))/(1+np.sin(t)*np.sin(t))
    y = (a*np.cos(t)*np.sin(t))/(1+np.sin(t)*np.sin(t))
    return list(map(add,(x,y),origo))

def calc_leminskata2(t,origo):
    a = 100
    x = (a*np.cos(t))/(1+np.sin(t)*np.sin(t))
    y = -(a*np.cos(t)*np.sin(t))/(1+np.sin(t)*np.sin(t))
    return list(map(add,(x,y),origo))

def calc_asteroid(t,origo):
    a = 50
    x = a*np.cos(t)**3
    y = a*np.sin(t)**3
    return list(map(add,(x,y),origo))

def calc_asteroid2(t,origo):
    a = 50
    x = a*np.cos(t)**3
    y = -a*np.sin(t)**3
    return list(map(add,(x,y),origo))

def plot_parabel(origo):
    tim.color('orange')
    tim.penup()
    tim.goto(calc_parabel(0,origo))
    tim.pendown()
    t= np.arange(0,2*np.pi,0.025)
    for i in t:
        tim.goto(calc_parabel(i,origo))

def plot_parabel2(origo):
    tim.color('orange')
    tim.penup()
    tim.goto(calc_parabel(0,origo))
    tim.pendown()
    t= np.arange(0,2*np.pi,0.025)
    for i in t:
        tim.goto(calc_parabel2(i,origo))

def plot_hyperbel(origo):
    tim.penup()
    tim.goto(calc_hyperbel(0,origo))
    tim.pendown()
    t = np.arange(0,np.pi,0.025)
    for i in t:
        tim.goto(calc_hyperbel(i,origo))
    
def plot_hyperbel2(origo):
    tim.penup()
    tim.goto(calc_hyperbel(0,origo))
    tim.pendown()
    t = np.arange(0,np.pi,0.025)
    for i in t:
        tim.goto(calc_hyperbel2(i,origo))
    
def plot_leminskata(origo):
    tim.penup()
    tim.goto(calc_leminskata(0,origo))
    tim.pendown()
    t = np.arange(0,np.pi,0.025)
    for i in t:
        tim.goto(calc_leminskata(i,origo))

def plot_leminskata2(origo):
    tim.penup()
    tim.goto(calc_leminskata(0,origo))
    tim.pendown()
    t = np.arange(0,np.pi,0.025)
    for i in t:
        tim.goto(calc_leminskata2(i,origo))
        
def plot_asteroid(origo):
    tim.penup()
    tim.goto(calc_asteroid(0,origo))
    tim.pendown()
    t = np.arange(0,np.pi,0.025)
    for i in t:
        tim.goto(calc_asteroid(i,origo))

def plot_asteroid2(origo):
    tim.penup()
    tim.goto(calc_asteroid(0,origo))
    tim.pendown()
    t = np.arange(0,np.pi,0.025)
    for i in t:
        tim.goto(calc_asteroid2(i,origo))

### Huvudprogram ###
tim = t.Turtle()
tim.hideturtle()
tim.pensize(6)
tim.shape("triangle")
tim.shapesize(0.4)
tim.speed(0)  # 0 - 10, 1 - 10 ökad hastighet, 0 snabbast
screen = t.Screen()
screen.bgcolor("Black")
screen.setup(900, 600)
screen.title("Några parametriska kurvor")

origo = (-300, 150)  # Runt vilken punkt plotten ska vara centererad
plot_ellipse(origo)  # Plottar ellipsen
print_text("Ellips", origo)  # Skriver texten i ellipsen
origo = (-150,150)
plot_parabel(origo)
origo = (-150,150)
plot_parabel2(origo)
origo = (50, 150)
plot_hyperbel(origo)
origo = (50,150)
plot_hyperbel2(origo)
origo = (-300,0)
plot_leminskata(origo)
plot_leminskata2(origo)
origo = (-150,0)
plot_asteroid(origo)
plot_asteroid2(origo)



screen.exitonclick()