from flask import render_template, flash, redirect    #导入模块，flash函数，redirect函数
from app import app
from .forms import LoginForm   #导入LoginForm类


@app.route('/login', methods = ['GET', 'POST'])   #这里'/login'表示的是，网页最后后缀是/login的时候，访问login.html页面
def login():
    form = LoginForm()                 #生成form实例，给render_template渲染使用
    if form.validate_on_submit():  # 调用form实例里面的validate_on_submit()功能，验证数据是否安全，如是返回True，默认返回False
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')  # 如果数据符合要求，重定向到主页
    return render_template('login.html', title = 'Sign In', form = form, providers = app.config['OPENID_PROVIDERS'])

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'} # fake user
    posts = [
        {'author': { 'nickname': 'John' },'body': 'Beautiful day in Portland!'},
        {'author': { 'nickname': 'Susan' },'body': 'The Avengers movie was so cool!'}
    ]
    return render_template("index.html", title = 'Home', user = user, posts = posts)

