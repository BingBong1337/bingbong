'''from socket import *
def connect_to_server():
    s = socket()                # Skapa ett socket-objekt
    # Ange IP-adress manuellt
    host = input("Ange serverns IP-adress:")
    # t.ex. "localhost" om servern körs på samma dator som klienten
    port = 12345                # Servern körs på port 12345
    s.connect((host, port))     # Anslut till servern
    return s
s = connect_to_server()
def main():
    mess = ''
    while mess != '1':
        b = s.recv(1024)            # Ta emot ett meddelande från servern
        msg = b.decode("utf-16")    # Gör om meddelandet från bytekod till vanlig text
        print(msg)
        msg = input("Skriv något till servern:")
        b = msg.encode("utf-16")
        s.send(b)
    s.close()   
main()
'''
from socket import *
from _thread import *
import time as t
def connect_to_server():    # samma som i tidigare exempel
    s = socket()
    host = input("Ange serverns IP-adress:")
    port = 12345
    s.connect((host, port))
    return s
conn = connect_to_server()
b = conn.recv(1024)
msg = b.decode('utf-16')
print(msg)

def reciever():
    global msg 
    b = conn.recv(1024)
    msg = b.decode("utf-16")
    print(msg)

def sender():
    msg = input("Skriv något till servern:")
    b = msg.encode("utf-16")
    conn.send(b)

while True:
    start_new_thread(reciever,())
    start_new_thread(sender,())
    
