from flask import Blueprint

from APP.ext import db
from APP.models import Cat

blue = Blueprint('blue',__name__)
def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/index/')
def index():
    return 'O(∩_∩)O哈哈~'

#添加：
@blue.route('/add/')
def add():
    cat = Cat()
    cat.name = 'Tom猫'
    db.session.add(cat)
    db.session.commit()
    return "添加成功"