import socket
import threading


#making the server
HOST = "127.0.0.1"
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()

clients=[]
nicknames = []


#broadcasting messages
def broadcast(message):
        for client in clients:
            client.send(message)

#handle multiple clients
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            print(f"{nickname} left the chat!".encode("ascii"))
            break

#recieve clients to the server
def recieve():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname of the client {nickname}")
        broadcast(f"{nickname} has joined to the chat!".encode("ascii"))
        client.send("You are Connected and Ready to Chat!".encode("ascii"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is Listning>>>>")
recieve()

        






