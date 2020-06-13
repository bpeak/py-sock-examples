import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 3000))

print("서버에 접속했습니다.")

f = open('send.jpg', 'rb')
buffer = b''
while True:
  data = f.read(1024)
  if not data:
    break
  buffer += data

f.close()

client_socket.sendall(buffer)

client_socket.close()
