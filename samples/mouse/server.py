import socket
import win32api
import time

HOST = '0.0.0.0'
PORT = 3000   

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
server_socket.bind((HOST, PORT))
server_socket.listen()

print("클라이언트를 기다리는중...")
client_socket, addr = server_socket.accept()
print("클라이언트{}가 연결했습니다.".format(addr))

prev_mouse_x = None
prev_mouse_y = None

while True:
  curr_mouse_x, curr_mouse_y = win32api.GetCursorPos()
  if prev_mouse_x and prev_mouse_y:
    diff_mouse_x = curr_mouse_x - prev_mouse_x
    diff_mouse_y = curr_mouse_y - prev_mouse_y
    client_socket.sendall("{},{}\r\n".format(diff_mouse_x, diff_mouse_y).encode())  
  prev_mouse_x = curr_mouse_x
  prev_mouse_y = curr_mouse_y  
  time.sleep(1 / 60)

client_socket.close()
server_socket.close()