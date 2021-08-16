import socket
import threading

HOST="127.0.0.1"
PORT = 55555

nickname =input("Choose a Nickname to Join the Chat: ")


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

#message recieving function
def recieve():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("Unfortunately, Something went Wrong!")
            client.close()
            break

#sending messages to the chat
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode("ascii"))

recieve_thread = threading.Thread(target= recieve)
recieve_thread.start()

write_thread = threading.Thread(target= write)
write_thread.start()



