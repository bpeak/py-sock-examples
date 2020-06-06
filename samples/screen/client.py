#!/usr/bin/python
import socket
import cv2
import numpy
import time
from PIL import ImageGrab

HOST = 'localhost'
PORT = 5001

sock = socket.socket()
sock.connect((HOST, PORT))
print("서버에 접속했습니다.")

while True:
  img=ImageGrab.grab() # 이미지 캡쳐
  data = numpy.array(img) # 2차원 배열로 변환
  stringData = data.tostring()
  sock.send(str(len(stringData)).ljust(16).encode()) # 길이먼저보냄
  sock.send(stringData) # 이미지데이터
  time.sleep(1)