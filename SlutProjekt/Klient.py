from tkinter import *
import _thread as th
import socket as so


def connect_to_server():
    s = so.socket()
    host = 'localhost'
    port = 12345
    s.connect((host, port))
    return s

s = connect_to_server()
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
    s.send(d)
    e.delete(0,1000)

name = Entry(root)
name.pack()

def receiver_thread():
    while True:
        b = s.recv(1024)
        msg = b.decode("utf-16")
        lbl["text"] = msg

th.start_new_thread(receiver_thread, ())
root.mainloop()


'''
def send():
    messageEntry = input()
    a = str(messageEntry).encode('utf-16')
    s.send(a)

def recieve():
    b = s.recv(1024)
    messages = b.decode('utf-16')
    print('recieved',messages)

s = connect_to_server()

while True:
    th.start_new_thread(send,())
    th.start_new_thread(recieve, ())
'''