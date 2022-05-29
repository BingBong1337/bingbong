#Imporar bibliotek som jag behöver använda mig av

from socket import *
from _thread import *

#Gör en funktion som startar servern
def start_server():         
    s = socket()
    host = "localhost"
    port = 12345
    s.bind((host, port))
    s.listen()
    return s


#Gör en funktion som konstant lyssnar på ingående medelanden
def threaded_client(conn):
    try:
        a = conn.recv(1024)
        msg = a.decode("utf-16")
        print(msg)
        #Om medelanded är det som skickas från funktionen Quitchat() i huvudprogramet stängs servern till användaren som lämnade chatten
        if msg == 'xqzwy':
            connections.remove(conn)
            ThreadCount = ThreadCount-1
            conn.close()
            
            
        else:
            #Annars skicks medelande till alla i chatten och kör om funktionen
            for i in connections:
                i.send(msg.encode('utf-16'))
                threaded_client(conn)
    except:
        pass
 
#Gör en lista och en counter för vilka som är här och hur många
connections = []
ThreadCount = 0

#Startar servern
s = start_server()

# Skapar en ny tråd för varje klient som ansluter
while True: 
    print("Väntar på att en klient ska ansluta till servern...")
    conn, address = s.accept()
    print("En ny klient anslöt: " + address[0] + ':'
          + str(address[1]))
    connections.append(conn)
    ThreadCount = len(connections)
    start_new_thread(threaded_client, (conn, ))
    print("Tråd nummer: " + str(ThreadCount))