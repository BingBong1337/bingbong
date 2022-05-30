from socket import *
from _thread import *
def start_server():
    s = socket()            # Skapa ett socket-objekt
    host = "10.32.39.186"      # som körs på den egna datorn
    port = 12345            # på port 12345.
    s.bind((host, port))    # Konfigurera socket-objektet.
    s.listen()              # Vänta på att klient ansluter.
    return s
s = start_server()
print("Väntar på att en klient ska ansluta till servern...")
conn, addr = s.accept()     # När en klient ansluter
print("En klient anslöt från adressen", addr)
msg = "Servern säger hej till klienten! Hur mår du idag?"
b = msg.encode("utf-16")    # Gör om meddelandet till bytekod
conn.send(b)                # Skicka meddelandet till klienten

def exit():
    quit = 'bye bye'
    quitt = quit.encode('utf-16')
    conn.send(quitt)
    conn.close()                # Stäng anslutningen till klienten

def reciever():
    global msg
    b = conn.recv(1024)         # Ta emot ett meddelande från klienten
    msg = b.decode("utf-16")    # Gör om från bytekod till vanlig text
    if msg != '':
        print(msg)
    if msg == '1':
        exiter()

def exiter():
    global msg
    if msg == '1':
        exit()

def sender():
    global mess
    mess = input('vad är ditt medelande?')
    mess = mess.encode('utf-16')
    conn.send(mess)

def main():
    global msg
    while True:
        start_new_thread(reciever,())
        start_new_thread(sender,())
   
main()

#10.32.39.186
