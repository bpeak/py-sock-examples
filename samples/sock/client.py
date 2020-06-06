import socket
import time

HOST = '127.0.0.1'  
PORT = 3000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

for i in range(10):
  client_socket.sendall(("안녕" + str(i)).encode())

client_socket.close()