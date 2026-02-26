import socket
import threading

HOST = 'localhost'
PORT = 3333

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg:
                print("Other:", msg)
        except:
            break

threading.Thread(target=receive, daemon=True).start()

while True:
    msg = input("Name: ")
    client.sendall(msg.encode())