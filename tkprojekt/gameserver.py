from concurrent.futures import thread
from multiprocessing import connection
import socket as so
import _thread as th

runda = 1

def start_server():
    s = so.socket()
    host = "10.32.39.186"
    port = 12345
    s.bind((host, port))
    s.listen()
    return s

def threaded_client(conn):
    global runda
    
    try:
        a = conn.recv(1024)
        msg = a.decode("utf-32")
        print(msg)
        for i in connections:
            if i == conn:
                print("samma connection!")
                continue
            if i == connections[0] and i == conn:
                connections[-1].send(msg.encode('utf-32'))
            if i == connections[-1]:
                connections[0].send(msg.encode('utf-32'))
            
    except: 
        pass

    runda += 1

    threaded_client(conn)

s = start_server()
ThreadCount = 0
connections = []

while ThreadCount < 2:
    print("Väntar på att en klient ska ansluta till servern...")
    conn, address = s.accept()
    print("En ny klient anslöt: " + address[0] + ':'
          + str(address[1]))
    th.start_new_thread(threaded_client, (conn, ))
    ThreadCount += 1
    connections.append(conn)
    print(connections)
    print("Tråd nummer: " + str(ThreadCount))

input()