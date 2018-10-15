from flask import Flask
from flask_session import Session

from App.views import blue




def create_app():
    app = Flask(__name__)
    #告诉你将session保存到哪一个数据库
    #如果你的redis服务没有设置开机启动 那么必须要在终端中 使用redis-server
    #如果不设置服务启动  那么会报错  no  na。。d  redis
    app.config['SECRET_KEY']='110'
    app.config['SESSION_KEY_PREFIX']='1806'
    app.config['SESSION_TYPE'] = 'redis'
    Session(app=app)
    # se = Session()
    # se.init_app(app=app)
    app.register_blueprint(blueprint=blue)
    return app