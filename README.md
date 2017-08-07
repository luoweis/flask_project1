# Flask

## 安装环境
```
安装pip
yum install pip
安装virtualenv
pip install virtualenv
创建一个虚拟环境
virtualenv venv
启动
source venv/bin/activate
退出
deactivate
```

### 安装必要的组件
```
pip install flask

pip freeze > requirements.txt
生成 requirements.txt 文件是为了让我们在部署这个应用的时候，可以更加方便的去安装所需要的软件包
#pip install -r requirements.txt
```

### GitHub 忽略文件
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
*.sage.py

# dotenv
.env

# virtualenv
.venv
venv/
ENV/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/

# mac
.idea/

```

## 创建应用
### 创建config.py文件
    该文件是整个flask应用程序的配置文件，Config/ProdConfig/DevConfig
```
class Config(object):
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    #Debug
    DEBUG = True
```

## 链接数据库
### mysql
    models 将关系型数据库转化成一个对象类型
    SQLALchemy是一个Python包，提供了对象关系映射（ORM）
#### 安装 SQLAlChemy
```
pip install flask-sqlalchemy
pip freeze > requirement.txt
```
    flask-sqlalchemy默认支持的sqlite，我们习惯使用mysql
    还需要使用sqlalchemy和mysql之间的连接器
```
    pip install PyMySQL
    pip freeze > requirements.txt
```

#### 定义mysql链接

    在config.py中定义链接URI
```
    class Config(object):
        pass
    class ProdConfig(Config):
        pass
    class DevConfig(Config):
        #Debug
        DEBUG = True
        SQLALCHEMY_TRACK_MODIFICATIONS = True
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cdb_outerroot:P@ssword!@#123@59560724aa35c.bj.cdb.myqcloud.com:8336/flask_project1'
```
#### SQLAlchemy的CRUD
    CRUD提供了在web应用程序中所需要的所有操作和检视数据的基础功能，尤其在REST风格的应用中，CRUD就能实现一切所需要的功能。
