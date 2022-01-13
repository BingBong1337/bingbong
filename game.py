import tkinter as tk
import random as r
root = tk.Tk()
re =True
w = tk.Canvas(root,bg = 'white',width=1920,height=1080)
w.place(x=0,y=0)
Game = False
Game_Start = False
Rock = False
Paper = False
Scissor = False
OppRock = False
OppScissor = False
OppPaper = False
OppWin = False
OppLoss = False


def RockF():
    global Rock
    Rock = True
    Game()
    return Rock

def PaperF():
    global Paper
    Paper = True
    Game()
    return Paper

def ScissorF():
    global Scissor
    Scissor = True
    Game()
    return Scissor



ShakeL = tk.PhotoImage(file = 'StenUppVänster.png')
ShakeR = tk.PhotoImage(file ='StenUppHöger.png')
Shake45L = tk.PhotoImage(file ='Sten45NerVänster.png')
Shake45R = tk.PhotoImage(file ='Sten45NerHöger.png')
StenL = tk.PhotoImage(file ='StenFrånVänster.png')
StenR = tk.PhotoImage(file ='StenFrånHöger.png')
SaxL = tk.PhotoImage(file ='SaxFrånVänster.png')
SaxR = tk.PhotoImage(file ='SaxFrånHöger.png')
PåseL = tk.PhotoImage(file ='PåseFrånVänster.png')
PåseR = tk.PhotoImage(file ='PåseFrånHöger.png')
Choose = tk.Label(root,text='Choose Rock, Paper Or Scissor')
Choose.place(x=700,y=0)
Sten = tk.Button(root,text = 'Rock',command = RockF)
Sten.place(x=500,y=700)
Påse = tk.Button(root,text = 'Paper',command = PaperF)
Påse.place(x=800,y=700)
Sax = tk.Button(root,text = 'Scissor',command = ScissorF)
Sax.place(x=1100,y=700)
def Swing():
    global lArm, rArm
    lArm.configure(image=Shake45L)
    lArm.place(x=200,y=300)
    rArm.configure(image=Shake45R)
    rArm.place(x=1000,y=300)

def downSwing():
    global lArm, rArm
    lArm.configure(image=StenL)
    lArm.place(x=0,y=500)
    rArm.configure(image=StenR)
    rArm.place(x=800,y=500)

def UpSwing():
    global lArm, rArm
    lArm.configure(image=ShakeL)
    lArm.place(x=200,y=0)
    rArm.configure(image=ShakeR)
    rArm.place(x=1200,y=0)

def ScissorL():
    global lArm
    lArm.configure(image=SaxL)
    lArm.place(x=0,y=500)

def ScissorR():
    global rArm
    rArm.configure(image=SaxR)
    rArm.place(x=800,y=500)

def RockL():
    global lArm
    lArm.configure(image=StenL)
    lArm.place(x=0,y=500)

def RockR():
    global rArm
    rArm.configure(image=StenR)
    rArm.place(x=800,y=500)

def PaperL():
    global lArm
    lArm.configure(image=PåseL)
    lArm.place(x=0,y=500)

def PaperR():
    global rArm
    rArm.configure(image=PåseR)
    rArm.place(x=800,y=500)

def Draw():
    draw = tk.Label(root,text='DRAW').place(x=200,y=200)
def loss():
    lossn = tk.Label(root,text='YOU LOSE').place(x=200,y=200)
def wins():
    win = tk.Label(root,text='YOU WIN').place(x=200,y=200)
   

def Animation():
    global lArm, rArm
    Sten.place_forget()
    Påse.place_forget()
    Sax.place_forget()
    Choose.place_forget()
    lArm = tk.Label(root,image = ShakeL)
    lArm.place(x=200,y=0)
    rArm = tk.Label(root,image = ShakeR)
    rArm.place(x=1200,y=0)
    root.after(100,Swing)
    root.after(200,downSwing)
    root.after(300,Swing)
    root.after(400,UpSwing)
    root.after(500,Swing)
    root.after(600,downSwing)
    root.after(700,Swing)
    root.after(800,UpSwing)
    root.after(900,Swing)
    if OppScissor == True:
        root.after(1000,ScissorR)
    elif OppPaper == True:
        root.after(1000,PaperR)
    else:
        root.after(1000,RockR)
    if Scissor == True:
        root.after(1000,ScissorL)
    elif Paper == True:
        root.after(1000,PaperL)
    else:
        root.after(1000,RockL)
    if OppRock == True and Scissor == True or OppPaper == True and Rock == True or OppScissor == True and Paper == True:
        root.after(1000,loss)
    elif OppRock == True and Rock == True or OppPaper == True and Paper == True or OppScissor == True and Scissor == True:
        root.after(1000,Draw)
    else:
         root.after(1000,wins)


        


def Game():
    global OppRock,OppScissor,OppPaper, OppRock,Scissor,OppPaper,Paper,OppScissor,Rock
    Opp = r.randint(0,2)
    if Opp == 0:
        OppRock = True
    elif Opp == 1:
        OppScissor = True
    else:
        OppPaper = True
    opponet = tk.Label(root,text='The Other ManGuy').place(x=1300,y=0)
  #  if OppRock == True and Scissor == True or OppPaper == True and Rock == True or OppScissor == True and Paper == True:
   #     loss()
    #elif OppRock == True and Rock == True or OppPaper == True and Paper == True or OppScissor == True and Scissor == True:
     #   Draw()
    #else:
     #   win = tk.Label(root,text='YOU WIN').place(x=200,y=200)
    Animation()
    
    #def bingbong():
    #    global Game
    #    Game = True
    #    b1.place_forget()
    #    Start.place_forget()
    #    print(Game)
    #    return Game


    #Start = tk.Label(root,text = 'Welcome to game')
    #Start.place(x=700,y=0)
    #b1 = tk.Button(root,text = 'bingbong',command = bingbong)
    #b1.place(x=700,y=300)


        

root.mainloop()
