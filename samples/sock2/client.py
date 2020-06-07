import socket
import time

HOST = '127.0.0.1'  
PORT = 3000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_socket.sendall(bytes([1, 2, 3, 4, 5, 6]))

client_socket.close()