from flask import Flask, redirect, url_for, render_template,request,session,flash,jsonify
from datetime import timedelta
from wtforms import Form, BooleanField, StringField, validators
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
RadioField, SelectField, TextAreaField,SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes=3)

app.secret_key = "#230dec61-fee8-4ef2-a791-36f9e680c9fc" #不加入會報錯
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        print("User entered: ", user)
        session["user"] = user
        session.permanent = True
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        print("session get" + str(user))
        return render_template("user.html",user=user)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

class RegForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/oldindex', methods=['GET','POST'])
def oldindex():
    """首頁"""
    username = False
    #form為類別的實體
    form = RegForm()
    if form.validate_on_submit():
        #取出username欄位的輸入值
        username = form.username.data
        #重設username欄位
        form.username.data = ''
    #將username與form帶入首頁home.html樣板中
    return render_template('oldhome.html', form=form,username=username)

class MyForm(FlaskForm):
    name = StringField('你的名字', validators=[DataRequired()])
    agreed = BooleanField('同意加入這個組織？')
    gender = RadioField('請輸入性別', choices=[('M','男生'),('F','女生')])
    hobby = SelectField('你的興趣', choices=[('sports','運動'),('travel','旅遊'),('movie','電影')])
    others= TextAreaField()
    submit = SubmitField("確認")
@app.route('/',methods=['GET','POST'])
def index():
    """首頁"""
    form = MyForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['agreed'] = form.agreed.data
        session['gender'] = form.gender.data
        session['hobby'] = form.hobby.data
        session['others'] = form.others.data
        return redirect(url_for('thankyou'))
    return render_template('home.html', form=form)

@app.route('/thankyou')
def thankyou():
    """thankyou頁"""
    return render_template('thankyou.html')

if __name__ == "__main__":
    app.run()