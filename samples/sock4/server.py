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

while True:
  send_text = input(">>>")
  send_text_bytes = send_text.encode('utf-8')
  conn_socket.sendall(send_text_bytes)

  # print("상대방이 입력중입니다...")
  recv_text_bytes = conn_socket.recv(1024)
  recv_text = recv_text_bytes.decode('utf-8')
  print("상대방 : {}".format(recv_text))

conn_socket.close()
server_socket.close()