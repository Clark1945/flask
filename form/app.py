from flask import Flask, redirect, url_for, render_template,request,session,flash,jsonify
from datetime import timedelta

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


if __name__ == "__main__":
    app.run(debug=True)