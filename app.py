from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__, static_folder='views/assets/')
@app.route('/hello/<name>')
def hello(name):
    return render_template('home.html',name = name)
@app.route("/hi/<name>")
def hi(name):
    return render_template("home.html",**locals()) #傳遞所有的參數與區域變數
# @app.route("/<name>")
# def home(name):
#     return f"{name}, Welcome. This is Home Page"

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


@app.route("/getname",methods=["GET","POST"])
def getname():
    name = request.args.get("name")
    return render_template("get.html",name=name)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/submit",methods=["POST"])
def submit():
    firstname = request.values['firstname']
    lastname = request.values['lastname']
    return render_template("submit.html",**locals())

@app.route("/form2", methods=["POST","GET"])
def form2():
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        return redirect(url_for('submit',**locals()))
    else:
        return render_template('form2.html')
# request.values： 它是 request 對象的屬性，用於獲取請求中的數據。request.values 包含所有提交的數據，不僅僅是表單數據，還包括 URL 中的查詢字符串數據。
# 它相當於 request.args（查詢字符串數據）和 request.form（表單數據）的合併。
# request.form： 它是 request 對象的屬性，專門用於獲取表單數據。
# request.form 只包含 POST 請求中提交的表單數據。
if __name__ == '__main__':
    app.run()