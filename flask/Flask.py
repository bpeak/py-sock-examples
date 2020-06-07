import socket

class Flask:
  def __init__(self, name):
    self.url_maps = {}
    pass

  def handle_request(self, url):
    response_func = self.url_maps.get(url)
    response_body = response_func()
    response = """
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2009 12:28:53 GMT
Server: Apache/2.2.14 (Win32)
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
Content-Length: {}
Content-Type: text/html; charset=utf-8
Set-Cookie: uuid=12313-abac-1234-asd
Connection: Closed

""".format(len(response_body)) + response_body
    response = response.strip()
    
    return response
    
  def route(self, url):
    def deco(func):
      def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
      self.url_maps[url] = wrapper
      return wrapper
    return deco

  def run(self, host='0.0.0.0', port=3000):
    while True:
      server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
      server_socket.bind((host, port))
      server_socket.listen()    

      print("클라이언트를 기다리는중...")
      conn_socket, addr = server_socket.accept()
      print("클라이언트{}가 연결했습니다.".format(addr))

      request_buffer = conn_socket.recv(65535)
      request = request_buffer.decode('utf-8')

      request_lines = request.split('\n')
      request_lines = [request_line for request_line in request_lines if request_line != "\r" and request_line != ""]
      request_line = request_lines[0]
      htt_method, url, http_version = request_line.split(" ")
      headers = request_lines[1:len(request_lines)]
      headers = [header[0:len(header) - 1].split(" ") for header in headers]
      headers = [{ "key": header[0], "value": header[1] } for header in headers]

      response = self.handle_request(url)
      response_buffer = response.encode('utf-8')

      conn_socket.sendall(response_buffer)

      conn_socket.close()
      server_socket.close()      

app = Flask(__name__)

@app.route("/test")
def main():
  return "<h1>메인</h1>"

@app.route("/boards")
def boards():
  return "<h1>boards...</h1>"

app.handle_request("/test")
app.handle_request("/boards")

app.run(host='0.0.0.0', port=3000)