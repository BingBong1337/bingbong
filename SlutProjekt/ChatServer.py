from socket import *
from _thread import *
def start_server():         # Samma som i förra exemplet
    s = socket()
    host = "localhost"
    port = 12345
    s.bind((host, port))
    s.listen()
    return s



def threaded_client(conn):
    try:
        a = conn.recv(1024)
        msg = a.decode("utf-16")
        print(msg)
        if msg == 'xqzwy':
            connections.remove(conn)
            ThreadCount = ThreadCount-1
            conn.close()
            
            
        else:
            for i in connections:
                i.send(msg.encode('utf-16'))
                threaded_client(conn)
    except:
        pass
 

connections = []
ThreadCount = 0

s = start_server()


while True: # Skapar en ny tråd för varje klient som ansluter
    print("Väntar på att en klient ska ansluta till servern...")
    conn, address = s.accept()
    print("En ny klient anslöt: " + address[0] + ':'
          + str(address[1]))
    connections.append(conn)
    ThreadCount = len(connections)
    start_new_thread(threaded_client, (conn, ))
    print("Tråd nummer: " + str(ThreadCount))