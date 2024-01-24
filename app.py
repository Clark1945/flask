from flask import Flask,render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return render_template('home.html',name = name)
@app.route("/hi/<name>")
def hi(name):
    return render_template("home.html",**locals()) #傳遞所有的參數與區域變數
@app.route("/<name>")
def home(name):
    return f"{name}, Welcome. This is Home Page"

@app.route("/greet")
def greet():
    list_foods = ['apple', 'banana', 'candy']
    dict_foods = {'food1': 'apple', 'food2': 'banana', 'food3': 'candy'}
    user = "Clark"
    return render_template("test.html",list_foods=list_foods,dict_foods=dict_foods,user=user)
@app.route("/base")
def base():
    return render_template("base.html",site_name="My Website")

@app.route("/halo/<name>")
def halo(name):
    return render_template("hello.html",name=name)

if __name__ == '__main__':
    app.run()