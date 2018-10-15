from flask import Blueprint, render_template, request, Response, redirect, url_for, session

blue = Blueprint('dage',__name__)

@blue.route('/')
def hello():
    session['name']='xiadajie'
    return '你说的不错报？'

'''
进入登录页面  登录之后显示 欢迎xxxx
'''

@blue.route('/toLogin/')
def toLogin():
    return render_template('login.html')

#视图函数返回Response对象

# @blue.route('/login/',methods = ['post'])
# def login():
#     #获取文本框中的内容
#     name = request.form.get('name')
#     res = Response('您的名字是%s' % name)
#     print(type(res))
#     return res

@blue.route('/login/',methods=['post','get'])
def login():
    name = request.form.get('name')
    response = redirect(url_for('dage.index'))
    response.set_cookie('name',name)
    return response

@blue.route('/index/')
def index():
   name = request.cookies.get('name','游客')
   res =  render_template('index.html',name = name)
   return res

@blue.route('/logout/')
def logout():

    response = redirect(url_for('dage.index'))

    response.delete_cookie('name')
    return response