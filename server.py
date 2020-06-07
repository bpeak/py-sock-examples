from flask import Flask
app = Flask(__name__)

@app.route("/test")
def main():
  return "<h1>메인</h1>"

@app.route("/boards")
def boards():
  return "<h1>boards...</h1>"

@app.route("/abc")
def abc():
  return "<button>test</button>"

app.run(host='0.0.0.0', port=3000)