import socket
import win32api
import time

HOST = '0.0.0.0'
PORT = 3000   

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
server_socket.bind((HOST, PORT))
server_socket.listen()

print("클라이언트를 기다리는중...")
conn_socket, addr = server_socket.accept()
print("클라이언트{}가 연결했습니다.".format(addr))

request_buffer = conn_socket.recv(65535)
request = request_buffer.decode('utf-8')

print(request)

response = """
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2009 12:28:53 GMT
Server: Apache/2.2.14 (Win32)
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
Content-Length: 47
Content-Type: text/html
Set-Cookie: uuid=12313-abac-1234-asd
Connection: Closed

<html>
  <body><h1>fuck you</h1></body>
</html>
""".strip()

response_buffer = response.encode('utf-8')

conn_socket.sendall(response_buffer)

conn_socket.close()
server_socket.close()