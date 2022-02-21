
from socket import *
def start_server():         # Samma som i förra exemplet
    s = socket()
    host = "10.32.39.186"
    port = 12345
    s.bind((host, port))
    s.listen()
    return s

def threaded_client(conn):
    global runda

    a = conn.recv(1024)
    msg = a.decode("utf-16")
    print(msg)
    for i in connections:
        if i == conn:
            pass
        else:
            i.send(msg.encode('utf-16'))
            


    threaded_client(conn)

s = start_server()
ThreadCount = 0
connections = []
        
from _thread import *
s = start_server()
ThreadCount = 0
while True: # Skapar en ny tråd för varje klient som ansluter
    print("Väntar på att en klient ska ansluta till servern...")
    conn, address = s.accept()
    print("En ny klient anslöt: " + address[0] + ':'
          + str(address[1]))
    start_new_thread(threaded_client, (conn, ))
    ThreadCount += 1
    print("Tråd nummer: " + str(ThreadCount))
