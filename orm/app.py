from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/MyFold/Programming_data/sqlite/flask_sample.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Mysqlroot13579@localhost:3306/data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 這個設定如果設置為True後Flask-SQLAlchemy為追蹤各種改變的信號，這樣子會消耗額外的記憶體，官網上建議如果沒有特別需要，可設定為關閉裝態。因此，在這裡我們設定為False。
db = SQLAlchemy(app)

Migrate(app,db)


class Task(db.Model):
    """Task DB"""
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    priority = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    remorks = db.Column(db.Text)
    # 一對一
    owner = db.relationship('Owner', backref='task', uselist=False)

    # 一對多
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))

    def __init__(self, name, priority, date, remorks):
        self.name = name
        self.priority = priority
        self.date = date
        self.remorks = remorks

class Owner(db.Model):
    """Owner DB"""
    __tablename__ = 'owners'
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(255))
    task_id   = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    def __init__(self, name, task_id):
        self.name    = name
        self.task_id = task_id

class Project(db.Model):
    """Project DB"""
    __tablename__ = 'projects'
    id          = db.Column(db.Integer, primary_key=True)
    proj_name   = db.Column(db.String(255))
    proj_status = db.Column(db.String(100))
    client_name = db.Column(db.String(100))
    org_name    = db.Column(db.String(255))
    task        = db.relationship('Task',backref='project', uselist=True)
    def __init__(self, proj_name, proj_status, client_name, org_name, task_id):
        self.proj_name   = proj_name
        self.proj_status = proj_status
        self.client_name = client_name
        self.org_name    = org_name
        self.task_id     = task_id