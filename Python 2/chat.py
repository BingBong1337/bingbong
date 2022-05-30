from socket import *
from tkinter import *
from _thread import *

def connect_to_server():    # samma som i tidigare exempel
    s = socket()
    host = input("Ange serverns IP-adress:")
    port = 12345
    s.connect((host, port))
    return s
    
conn = connect_to_server()

root = Tk()
root.geometry('400x700')

def chatting():
    global name, e,lbl
    e = Entry(root)
    e.pack()
    lbl = Label(root)
    lbl.pack()
    b = Button(root, text ="Skicka",command = click_handler)
    b.pack()

def setname():
    global x
    x = name.get()
    name.pack_forget()
    g.pack_forget()
    chatting()

g = Button(root,text = 'setname',command = setname)
g.pack()

def click_handler():
    msg = e.get()
    b = msg
    c = (f'{x}: {b}')
    d = c.encode("utf-16") 
    conn.send(d)
    e.delete(0,1000)

name = Entry(root)
name.pack()

def receiver_thread():
    while True:
        b = conn.recv(1024)
        msg = b.decode("utf-16")
        lbl["text"] = msg

start_new_thread(receiver_thread, ())
root.mainloop()