from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class Astock(db.Model):
    __tablename__ = 'astock'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stockid = db.Column(db.String(64))
    stockname = db.Column(db.String(64))
    company = db.Column(db.String(64))
    createtime = db.Column(db.String(64))
    category = db.Column(db.String(64))
    desc = db.Column(db.Text)
    baseInfo = db.relationship("Basicinfo", back_populates="name")

class Basicinfo(db.Model):
    __tablename__ = "basicinfo"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    Province = db.Column(db.String(256))
    company_id = db.Column(db.Integer,db.ForeignKey("astock.id"))
    name = db.relationship("Astock", back_populates="baseInfo")

class Company(db.Model):
    # 定义表名
    __tablename__ = 'company'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    province = db.Column(db.String(64))
    count = db.Column(db.Integer)

class Lianinfo(db.Model):
    __tablename__ = "lianinfo"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    dayNum = db.Column(db.Integer)
    lianNum = db.Column(db.Integer)
    weiJieNum = db.Column(db.Integer)

# Create the database tables.
db.create_all()

if __name__ == '__main__':
    app.run()