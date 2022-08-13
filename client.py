from email import message
from http import client
import socket
import time

HEADER =  64
PORT = 5050
FORMAT  = 'utf-8'
DISCONNECT_MSG = '!DISCONNECT'
SERVER = "127.0.1.1"
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("HELLO WORLD!")
send("HELLO E!")
send("HELLO LG!")

send(DISCONNECT_MSG)