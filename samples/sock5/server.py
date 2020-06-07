import socket
import win32api
import time
import threading

HOST = '0.0.0.0'
PORT = 3000   

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
server_socket.bind((HOST, PORT))
server_socket.listen()

print("클라이언트를 기다리는중...")
conn_socket, addr = server_socket.accept()
print("클라이언트{}가 연결했습니다.".format(addr))

def send(socket):
  while True:
    send_text = input(">>>")
    send_text_bytes = send_text.encode('utf-8')
    socket.sendall(send_text_bytes)  

def receive(sock):
  while True:
    recv_text_bytes = conn_socket.recv(1024)
    recv_text = recv_text_bytes.decode('utf-8')
    print("상대방 : {}".format(recv_text))  

send_thread = threading.Thread(target=send, args=(conn_socket, ))
receive_thread = threading.Thread(target=receive, args=(conn_socket, ))

send_thread.start()
receive_thread.start()

while True:
  time.sleep(1)