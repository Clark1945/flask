from flask import Flask, render_template, session, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/MyFold/Programming_data/sqlite/flask_sample.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 這個設定如果設置為True後Flask-SQLAlchemy為追蹤各種改變的信號，這樣子會消耗額外的記憶體，官網上建議如果沒有特別需要，可設定為關閉裝態。因此，在這裡我們設定為False。
db = SQLAlchemy(app)

app.secret_key = "#230dec61-fee8-4ef2-a791-36f9e680c9fc" #不加入會報錯

class Users(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email = db.Column(db.String(100))
    def __init__(self, name, email):
        self.name =name
        self.email = email

class Players(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'使用者名稱為 {self.name} ，年齡為 {self.age} 歲。'



# 在需要的地方建立所有表格
@app.route('/create_tables')
def create_tables():
    with app.app_context():
        db.create_all()
    return 'Tables created successfully!'

@app.route("/user", methods=["POST","GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = Users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()

        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email)
    else:
        return redirect(url_for("login"))

@app.route("/view")
def view():
    return render_template("view.html", values=Users.query.all())


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True # 瀏覽器關閉後依然保存
        user = request.form["nm"]
        session["user"] = user

        found_user = Users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = Users(user, "")
            db.session.add(usr)
            db.session.commit()

        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

###
basedir = os.path.abspath(os.path.dirname(__file__))
Migrate(app,db)


if __name__ =="__main__":
    app.run(debug=True)