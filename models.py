# -*- coding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from main import app

#初始化数据库
#SQLAlchemy会自动从app对象中的DevConfig中加载链接数据库的配置项
db = SQLAlchemy(app)


class User(db.Model):
    #定义表的名字
    __tablename__ = "users"
    id = db.Column(db.String(45),primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self,username):
        self.username = username

    def __repr__(self):
        return "<Model User '{}'>" .format(self.username)

#基于users表
#有三个字段
#id
#username
#password

