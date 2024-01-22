from flask import Flask

app = Flask(__name__)

@app.route("/hi")
@app.route('/hello')
def hello():
    return 'Hello World!'
@app.route("/<name>")
def home(name):
    return f"{name}, Welcome. This is Home Page"

if __name__ == '__main__':
    app.run()