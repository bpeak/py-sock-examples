import socket
import time
import win32api
import time

HOST = '127.0.0.1'  
PORT = 3000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
client_socket.connect((HOST, PORT))
print("서버에 접속했습니다.")

coors = []

while True:
  data = client_socket.recv(1024)
  data = data.decode()
  coors = coors + [map(int, v.split(",")) for v in data.split("\r\n") if v]
  while len(coors) != 0:
    dx, dy = coors.pop(0)
    prev_mouse_x, prev_mouse_y = win32api.GetCursorPos()
    win32api.SetCursorPos((prev_mouse_x + dx, prev_mouse_y + dy))

client_socket.close()

