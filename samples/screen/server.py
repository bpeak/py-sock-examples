import socket
import cv2
import numpy

HOST = '0.0.0.0'
PORT = 5001

#socket 수신 버퍼를 읽어서 반환하는 함수
def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(True)
print("클라이언트의 접속을 기다리고있습니다.")
client_socket, addr = server_socket.accept()
print("클라이언트 {}가 접속했습니다.".format(addr))

while True:
    length = recvall(client_socket, 16) # 이미지 길이 먼저 수신
    stringData = recvall(client_socket, int(length)) # 이미지 수신
    data = numpy.frombuffer(stringData, dtype='uint8') # unsigned int

    data = data.reshape(1080, 1920, 3)

    cv_img = cv2.cvtColor(data, cv2.COLOR_RGB2BGR)
    # cv_img = cv2.resize(cv_img, (960, 540))
    cv2.imshow('CLIENT', cv_img)
    cv2.waitKey(1)

cv2.destroyAllWindows()