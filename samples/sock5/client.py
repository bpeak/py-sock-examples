import socket
import time
import threading

HOST = '127.0.0.1'  
PORT = 3000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("서버에 접속했습니다. ")

def send(socket):
  while True:
    send_data = input('>>>')
    send_data_bytes = send_data.encode('utf-8')
    socket.send(send_data_bytes)

def receive(socket):
  while True:
    recv_text_bytes = socket.recv(1024)
    print("상대방: {}".format(recv_text_bytes.decode('utf-8')))

send_thread = threading.Thread(target=send, args=(client_socket, ))
receive_thread = threading.Thread(target=receive, args=(client_socket, ))

send_thread.start()
receive_thread.start()

while True:
  time.sleep(1)