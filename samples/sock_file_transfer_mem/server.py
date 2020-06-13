import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 3000))
server_socket.listen()

print("클라이언트를 기다리는중")
client_socket, addr = server_socket.accept()
print("client {} 가 접속했습니다.".format(addr))

f = open('recv.jpg', 'wb')

while True:
  byte_data = client_socket.recv(1024)
  if not byte_data:
    break
  print("readed 1024bytes...")
  f.write(byte_data)

f.close()


client_socket.close()
server_socket.close()