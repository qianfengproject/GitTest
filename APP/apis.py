from flask import Blueprint

blue = Blueprint('blue',__name__)

@blue.route('/index/')
def index():
    return 'O(∩_∩)O哈哈~'