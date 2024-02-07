from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/MyFold/Programming_data/sqlite/flask_sample.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 這個設定如果設置為True後Flask-SQLAlchemy為追蹤各種改變的信號，這樣子會消耗額外的記憶體，官網上建議如果沒有特別需要，可設定為關閉裝態。因此，在這裡我們設定為False。
db = SQLAlchemy(app)

Migrate(app,db)
class Players(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    email = db.Column(db.Text)
    nickname = db.Column("player_nickname",db.String(100))

    def __init__(self, name, age,email):
        self.name = name
        self.age = age
        self.email=email

    def __repr__(self):
        return f'使用者名稱為 {self.name} ，年齡為 {self.age} 歲。'
