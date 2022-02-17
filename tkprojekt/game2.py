import tkinter as tk
import random as r
import socket as so

arena = tk.Tk()
arena.geometry('900x540')

rockimg = tk.PhotoImage(file = 'tkprojekt/bilder/rock.png')
rockimg = rockimg.subsample(7,7)
rockimg = rockimg.subsample(3,3)
rockimg = rockimg.zoom(3,3)
paperimg = tk.PhotoImage(file = 'tkprojekt/bilder/paper.png')
paperimg = paperimg.subsample(11,11)
paperimg = paperimg.subsample(3,3)
paperimg = paperimg.zoom(3,3)
scissorsimg = tk.PhotoImage(file = 'tkprojekt/bilder/scissors.png')
scissorsimg = scissorsimg.subsample(10,10)
scissorsimg = scissorsimg.subsample(3,3)
scissorsimg = scissorsimg.zoom(3,3)
tableimg = tk.PhotoImage(file = 'tkprojekt/bilder/table2.png')
tableimg = tableimg.subsample(3,3)
tableimg = tableimg.zoom(3,3)
winimg = tk.PhotoImage(file = 'tkprojekt/bilder/youwin.png')
loseimg = tk.PhotoImage(file = 'tkprojekt/bilder/youlose.png')
playbimg = tk.PhotoImage(file = 'tkprojekt/bilder/playb.png')
playbimg = playbimg.subsample(20,20)
playbimg = playbimg.subsample(3,3)
playbimg = playbimg.zoom(3,3)
perimg = tk.PhotoImage(file = 'tkprojekt/bilder/per.png')
perimg = perimg.subsample(3,3)
perimg = perimg.subsample(3,3)
perimg = perimg.zoom(3,3)
menuimg = tk.PhotoImage(file = 'tkprojekt/bilder/menuscreen.png')
menuimg = menuimg.subsample(3,3)
menuimg = menuimg.zoom(3,3)
background2 = tk.PhotoImage(file = 'tkprojekt/bilder/backround 2.png')
background2 = background2.subsample(3,3)
background2 = background2.zoom(3,3)

enemyscore = 0
playerscore = 0
rockY = 450
paperY = 450
scissorsY = 450
jonasY = 240

playvar = 0
runvar = 0

rint = 0

jonasvar = 0
safejonas = 0

scoremax = 3

def connect_to_server():
    s = so.socket()
    print(serverid.get())
    host = serverid.get()
    port = 12345
    s.connect((host, port))
    return s

def start():
    global s
    provisional = False
    try:
        connect_to_server()
        s = connect_to_server()
        provisional = True
    except:
        pass

    if provisional == True:
        startbutton.place_forget()

        rockb.place(anchor = tk.CENTER, x = 200, y = 517)
        paperb.place(anchor = tk.CENTER, x = 450, y = 517)
        scissorsb.place(anchor = tk.CENTER, x = 700, y = 517)
        playb.place(anchor = tk.CENTER, x = 450, y = 270)

        gameloop()
        serverid.delete(0,1000)
    
def rockf():
    global playvar
    playvar = 1

def paperf():
    global playvar
    playvar = 2

def scissorsf():
    global playvar
    playvar = 3

def play():
    global runvar, playvar
    if playvar != 0:
        runvar = 1
        playb.place_forget()
        rockb.place_forget()
        paperb.place_forget()
        scissorsb.place_forget()
        resetb.place_forget()
        arena.after(2200, func = hismove)

def spawnrb():
    global playerscore, enemyscore, scoremax
    if playerscore == scoremax or enemyscore == scoremax:
        pass
    else:
        resetb.place(anchor = tk.CENTER, x = 450, y = 400)

def jonasplus():
    global enemyscore
    enemyscore += 1

def playerplus():
    global playerscore
    playerscore += 1

def draw2():
    global playerscore
    playerscore += 0

def hismove():
    global rint, jonasvar, enemyscore, playerscore
    jonasvar = 1

    rint = r.randint(1,3)

    if playvar == 1:
        if rint == 1:
            arena.after(1300, func = draw2)
        elif rint == 2:
            arena.after(1300, func = jonasplus)
        elif rint == 3:
            arena.after(1300, func = playerplus)

    elif playvar == 2:
        if rint == 1:
            arena.after(1300, func = playerplus)
        elif rint == 2:
            arena.after(1300, func = draw2)
        elif rint == 3:
            arena.after(1300, func = jonasplus)

    elif playvar == 3:
        if rint == 1:
            arena.after(1300, func = jonasplus)
        elif rint == 2:
            arena.after(1300, func = playerplus)
        elif rint == 3:
            arena.after(1300, func = draw2)

    arena.after(1300, func = spawnrb)

def reset():
    global rockY, paperY, scissorsY, jonasY, rvar, pvar, svar, playvar, runvar, rint, jonasvar, safejonas
    rockb.place(anchor = tk.CENTER, x = 200, y = 517)
    paperb.place(anchor = tk.CENTER, x = 450, y = 517)
    scissorsb.place(anchor = tk.CENTER, x = 700, y = 517)
    playb.place(anchor = tk.CENTER, x = 450, y = 270)

    rockY = 450
    paperY = 450
    scissorsY = 450
    jonasY = 240

    rvar = 0
    pvar = 0
    svar = 0

    playvar = 0
    runvar = 0

    rint = 0

    jonasvar = 0
    safejonas = 0

    resetb.place_forget()

def draw():
    global rvar, pvar, svar, rockY, paperY, scissorsY, jonasY, safejonas, enemyscore, playerscore, scoremax
    canvas.create_image(450, 270, anchor = tk.CENTER, image = background2)
    if enemyscore == scoremax:
        canvas.create_image(450, 270, anchor = tk.CENTER, image = loseimg)
    elif playerscore == scoremax:
        canvas.create_image(450, 270, anchor = tk.CENTER, image = winimg)
    elif runvar == 0:
        canvas.create_image(450, 240, anchor = tk.CENTER, image = perimg)
        canvas.create_image(450, 600, anchor = tk.CENTER, image = tableimg)
        canvas.create_image(200, rockY, anchor = tk.CENTER, image = rockimg)
        canvas.create_image(450, paperY, anchor = tk.CENTER, image = paperimg)
        canvas.create_image(700, scissorsY, anchor = tk.CENTER, image = scissorsimg)
    elif runvar == 1:
        canvas.create_image(450, jonasY, anchor = tk.CENTER, image = perimg)
        canvas.create_image(450, 600, anchor = tk.CENTER, image = tableimg)
        if playvar == 1:
            canvas.create_image(200, rockY, anchor = tk.CENTER, image = rockimg)
        elif playvar == 2:
            canvas.create_image(450, paperY, anchor = tk.CENTER, image = paperimg)
        elif playvar == 3:
            canvas.create_image(700, scissorsY, anchor = tk.CENTER, image = scissorsimg)
    if enemyscore == scoremax:
        canvas.create_text(450, 460, anchor = tk.CENTER, text = f'final score: {enemyscore} - {playerscore}.')
    elif playerscore == scoremax:
        canvas.create_text(450, 460, anchor = tk.CENTER, text = f'final score: {playerscore} - {enemyscore}.')
    else:
        canvas.create_text(50, 25, anchor = tk.CENTER, text = f'Enemy: {enemyscore}')
        canvas.create_text(850, 25, anchor = tk.CENTER, text = f'You: {playerscore}')

    #update rock place
    if playvar == 1:
        if rockY >= 435:
            rockY -= 5
        else:
            pass
    else:
        if rockY == 450:
            pass
        else:
            rockY += 5

    #update paper place
    if playvar == 2:
        if paperY >= 435:
            paperY -= 5
        else:
            pass
    else:
        if paperY == 450:
            pass
        else:
            paperY += 5

    #update scissors place
    if playvar == 3:
        if scissorsY >= 435:
            scissorsY -= 5
        else:
            pass
    else:
        if scissorsY == 450:
            pass
        else:
            scissorsY += 5
    
    #update jonas place
    if jonasvar == 1:
        if jonasY < 280 and safejonas == 0:
            jonasY += 8
        elif jonasY > 240:
            safejonas = 1
            jonasY -= 5
    
    if rint == 1 and safejonas == 1:
        if playerscore == scoremax:
            pass
        elif enemyscore == scoremax:
            pass
        else:
            canvas.create_image(220, 280, anchor = tk.CENTER, image = rockimg)
    elif rint == 2 and safejonas == 1:
        if playerscore == scoremax:
            pass
        elif enemyscore == scoremax:
            pass
        else:
            canvas.create_image(220, 285, anchor = tk.CENTER, image = paperimg)
    elif rint == 3 and safejonas == 1:
        if playerscore == scoremax:
            pass
        elif enemyscore == scoremax:
            pass
        else:
            canvas.create_image(220, 290, anchor = tk.CENTER, image = scissorsimg)
    else:
        pass

def gameloop():
    canvas.delete("all")
    draw()
    canvas.update()
    arena.after(17, func = gameloop)

canvas = tk.Canvas(arena, width = 900, height = 540, bg = 'white', bd = 0)
canvas.pack()

canvas.create_image(450, 270, anchor = tk.CENTER, image = menuimg)
canvas.create_text(450, 50, anchor = tk.CENTER, text = 'Welcome to')
canvas.create_text(450, 70, anchor = tk.CENTER, text = 'RPS Online', font = 30)
canvas.create_text(450, 220, anchor = tk.CENTER, text = 'Join Game', font = 15)

startbutton = tk.Button(arena, image = playbimg, bd = 0, command = start)
startbutton.place(anchor = tk.CENTER, x = 450, y = 270)

canvas.create_text(450, 310, anchor = tk.CENTER, text = 'Server IP', font = 15, fill = 'white')
serverid = tk.Entry(arena)
serverid.place(anchor = tk.CENTER, x = 450, y = 330)

rockb = tk.Button(arena, text = 'rock', bd = 1, command = rockf)
paperb = tk.Button(arena, text = 'paper', bd = 1, command = paperf)
scissorsb = tk.Button(arena, text = 'scissors', bd = 1, command = scissorsf)
playb = tk.Button(arena, text = 'play', bd = 1, command = play)
resetb = tk.Button(arena, text = 'playnext', bd = 1, command = reset)


arena.mainloop()