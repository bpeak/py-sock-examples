import socket
import time

HOST = '127.0.0.1'  
PORT = 3000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("서버에 접속했습니다. ")

while True:
  # print("상대방이 입력중입니다...")
  recv_text_bytes = client_socket.recv(1024)
  print("상대방: {}".format(recv_text_bytes.decode('utf-8')))

  send_data = input('>>>')
  send_data_bytes = send_data.encode('utf-8')
  client_socket.send(send_data_bytes)


client_socket.close()