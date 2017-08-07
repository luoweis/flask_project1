class Config(object):
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    #Debug
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cdb_outerroot:P@ssword!@#123@59560724aa35c.bj.cdb.myqcloud.com:8336/flask_project1'