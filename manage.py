# -*- coding:utf-8 -*-
from flask_script import Manager
from flask_script import Server
import main
import models
#初始化 app对象
manager = Manager(main.app)

manager.add_command("server",Server())

@manager.shell
def make_shell_context():
    #确保有导入Flask app object ，否则启动的CLI上下文中仍然没有app对象
    return dict(app=main.app,
                db=models.db,
                User=models.User)
    #在models.py中新定义一个数据模型，都需要在manager.py中导入并添加到返回dict中
    #使用 python manager.py shell 进行数据库表的创建

if __name__ == "__main__":
    manager.run()