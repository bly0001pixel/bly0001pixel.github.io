import socket
import threading

HOST = 'localhost'
PORT = 3333

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def handle_clients(client):
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
            for c in clients:
                if c != client:
                    c.sendall(data)
        except:
            break
    client.close()
    clients.remove(client)

print("Server running...")
while True:
    client, addr = server.accept()
    print(f"Connected: {addr}")
    clients.append(client)
    threading.Thread(target=handle_clients, args=(client,), daemon=True).start()