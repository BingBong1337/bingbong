from socket import *
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
def main():
    mess = ''
    
    while mess != '1':
        print("Väntar på meddelande från klienten...")
        b = conn.recv(1024)         # Ta emot ett meddelande från klienten
        msg = b.decode("utf-16")    # Gör om från bytekod till vanlig text
        if msg == '1':
            quit = 'bye bye'
            quitt = quit.encode('utf-16')
            conn.send(quitt)
            conn.close()                # Stäng anslutningen till klienten
        if msg != '1':
            print(msg)
            mess = input('vad är ditt medelande?')
            msg = mess.encode('utf-16')
            conn.send(msg)
        
   
main()

#10.32.39.186