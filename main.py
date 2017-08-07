# -*- coding:utf-8 -*-
from flask import Flask
from config import DevConfig
app = Flask(__name__)


#加载开发配置
app.config.from_object(DevConfig)

#"／"的路由规则
@app.route('/')
def home():
    return "<h1>Hello World!</h1>"


if __name__ == "__main__":
    app.run()
