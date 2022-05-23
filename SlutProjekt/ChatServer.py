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
        for i in connections:
            #if i == conn:
             #   pass
           # else:
            i.send(msg.encode('utf-16'))
    except:
        pass


    threaded_client(conn)


ThreadCount = 0
connections = []
        

s = start_server()


while True: # Skapar en ny tråd för varje klient som ansluter
    print("Väntar på att en klient ska ansluta till servern...")
    conn, address = s.accept()
    print("En ny klient anslöt: " + address[0] + ':'
          + str(address[1]))
    connections.append(conn)
    start_new_thread(threaded_client, (conn, ))
    ThreadCount += 1
    print("Tråd nummer: " + str(ThreadCount))