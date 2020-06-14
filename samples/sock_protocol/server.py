import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 3000))
server_socket.listen()

print("클라이언트를 기다리는중...")
conn_socket, addr = server_socket.accept()
print("클라이언트 {} 접속".format(addr))

buffer = conn_socket.recv(65536)
request = buffer.decode('utf-8')
request_lines = request.strip().split("\n")
for request_line in request_lines:
  key, value = request_line.split(": ")
  print("key: {}, value: {}".format(key, value))

conn_socket.close()
server_socket.close()