import os


CSRF_ENABLED = True		#激活跨站点请求伪造保护
# 当CSRF激活的时候才需要，它是用来建立一个加密的令牌，用于验证一个表单
SECRET_KEY = 'shi-yan-lou' 

basedir = os.path.abspath(os.path.dirname(__file__))
# 存储我们数据库文件的路径
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')
# 存储SQLAlchemy-migrate数据文件
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_respository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# print (basedir)
# print (SQLALCHEMY_MIGRATE_REPO)
# print (SQLALCHEMY_DATABASE_URI)
