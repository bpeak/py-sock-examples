import socket
import time

HOST = '127.0.0.1'  
PORT = 3000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# # < 1글자 전송 >
# print("가".encode("utf-8"))
# client_socket.sendall(("가").encode("utf-8"))

# # < 반복 전송 >
# for i in range(10):
#   client_socket.sendall(("가").encode("utf-8"))
#   # client_socket.sendall(("가" + str(i)).encode("utf-8"))

# < 입력한 글자 전송 >
print("보낼메시지를 입력해주세요.")
text = input()
print(text.encode("utf-8"))
client_socket.sendall((text).encode("utf-8"))

client_socket.close()