import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 3000))
server_socket.listen()

print("클라이언트를 기다리는중")
client_socket, addr = server_socket.accept()
print("client {} 가 접속했습니다.".format(addr))

buffer = b''
while True:
  data = client_socket.recv(1024)
  if not data:
    break
  print("readed 1024bytes...")
  buffer += data

f = open('recv.jpg', 'wb')
f.write(buffer)
f.close()

client_socket.close()
server_socket.close()