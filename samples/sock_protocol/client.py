import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 3000))

request = """
filename: 곰돌이.jpg
myname: kihyun
downloadSpeed: fast
""".strip()

request_bytes = request.encode()

client_socket.sendall(request_bytes)

client_socket.close()