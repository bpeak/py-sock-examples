import socket
import win32api
import time

HOST = '0.0.0.0'
PORT = 3000   

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
server_socket.bind((HOST, PORT))
server_socket.listen()

print("클라이언트를 기다리는중...")
client_socket, addr = server_socket.accept()
print("클라이언트{}가 연결했습니다.".format(addr))

buffer = b""
while True:
  byte = client_socket.recv(1)
  print("byte :", byte)
  if byte:
    buffer += byte
  else:
    break

print("buffer : ", buffer)
print("text : ", buffer.decode("utf-8"))

client_socket.close()
server_socket.close()