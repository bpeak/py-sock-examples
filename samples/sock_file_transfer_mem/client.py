import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 3000))

print("서버에 접속했습니다.")

f = open('send.jpg', 'rb')

while True:
  byte_data = f.read(1024)
  if not byte_data:
    break
  print("send 1024bytes...")
  client_socket.sendall(byte_data)

client_socket.close()
