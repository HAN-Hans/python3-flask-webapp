# -*- coding:utf8 -*-
import sys
sys.path.append('D:\\python3-flask-webapp\\micblog')



import datetime
from flask import render_template,flash,redirect,session,url_for,request,g
from flask_login import login_user,logout_user,current_user,login_required 
from app.models import User,Post,ROLE_USER,ROLE_ADMIN
from app import app,db,lm
from app.forms import LoginForm,SignUpForm,AboutMeForm,PublishBlogForm
from app.utils import PER_PAGE





@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
@app.route('/index')
def index():
    user = 'Justin Han'
    posts = [
        {
            'author': {'nickname': 'John'},

            'body': 'Beautiful day in Portland!'
        },

        {
            'author': {'nickname': 'Susan'},

            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template(
        "index.html",
        title = "Home",
        user = user,
        posts = posts)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    # 验证用户是否被验证
    if current_user.is_authenticated:
        return redirect('index')
    # 注册验证
    form = LoginForm()
  	# 如果 validate_on_submit 在表单提交请求中被调用，
   	# 它将会收集所有的数据，对字段进行验证，
   	# 如果所有的事情都通过的话，它将会返回 True，表示数据都是合法的。
   	# 这就是说明数据是安全的，并且被应用程序给接受了。
    if form.validate_on_submit():
        user = User.login_check(request.form.get('user_name'))
        if user:
            login_user(user)
            user.last_seen = datetime.datetime.now()

            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("The Database error!")
                return redirect('/login')

            flash('Your name: ' + request.form.get('user_name'))
            flash('remember me? ' + str(request.form.get('remember_me')))
            return redirect(url_for("users", user_id=current_user.id))
        else:
            flash('Login failed, Your name is not exist!')
            return redirect('/login')

    return render_template(
        'login.html', 
        title = 'Sign In',
        form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    user = User()
    if form.validate_on_submit():
        user_name = request.form.get('user_name')
        user_email = request.form.get('user_email')

        register_check = User.query.filter(db.or_(
            User.nickname == user_name, User.email == user_email)).first()
        if register_check:
            flash("error: The user's name or email already exists!")
            return redirect('/sign-up')

        if len(user_name) and len(user_email):
            user.nickname = user_name
            user.email = user_email
            user.role = ROLE_USER
            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("The Database error!")
                return redirect('/sign-up')

            flash("Sign up successful!")
            return redirect('/index')

    return render_template(
        "sign_up.html",
        title = 'Sign Up',
        form = form)


@app.route('/user/<int:user_id>',methods = ["POST","GET"])
@login_required
def users(user_id):
    form = AboutMeForm()
    user = User.query.filter(User.id == user_id).first()

    if not user:
        flash("The user is not exist")
        redirect('/index')
    blogs = user.posts.all()

    return render_template(
        "user.html",
        form=form,
        user=user,
        blogs=blogs) 


@app.route('/user/about-me/<int:user_id>', methods=["POST", "GET"])
@login_required
def about_me(user_id):
    user = User.query.filter(User.id == user_id).first()
    if request.method == "POST":
        content = request.form.get("describe")
        if len(content) and len(content) <= 140:
            user.about_me = content
            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("Database error!")
                return redirect(url_for("users", user_id=user_id))
        else:
            flash("Sorry, May be your data have some error.")
    return redirect(url_for("users", user_id=user_id))


@app.route('/publish/<int:user_id>', methods = ["POST", "GET"])
@login_required
def publish(user_id):
    form = PublishBlogForm()
    posts = Post()
    if form.validate_on_submit():
        blog_body = request.form.get("body")
        if not len(blog_body.strip()):
            flash("The content is necessray!")
            return redirect(url_for("publish", user_id=user_id))
        posts.body = blog_body
        posts.timestamp = datetime.datetime.now()
        posts.user_id = user_id

        try:
            db.session.add(posts)
            db.session.commit()
        except:
            flash("Database error!")
            return redirect(url_for("publish", user_id=user_id))

        flash("Publish Successful!")
        return redirect(url_for("publish", user_id=user_id))

    return render_template(
        "publish.html",
        form=form)


# @app.route('/user/<int:user_id>', default = {'page':1}, methods = ['POST','GET'])
# @app.route('/user/<int:user_id>/page/<int:page>', methods = ['GET','POST'])
# @login_required
# def users(user_id,page):
#     form = AboutMeForm()
#     if user_id != current_user.id:
#         flash('Sorry you can only view your own profile!','error')
#         return redirect('index')
    
#     #blogs = user.posts.paginate(page, PER_PAGE, False).items
#     pagination = Post.query.filter_by(user_id = current_user.id).order_by(
#         db.desc(Post.timestamp)).paginete(page, PER_PAGE, False)        
    
#     return render_template(
#         'user.html',
#         form = form,
#         pagination = pagination)





'''
为了渲染模板,我们必须从Flask框架中导入一个名为render_template 的新函数。
此函数需要传入模板名以及一些模板变量列表，返回一个所有变量被替换的渲染的模板。

在内部，render_template 调用了 Jinja2 模板引擎，J
inja2 模板引擎是 Flask 框架的一部分。
Jinja2 会把模板参数提供的相应的值替换了 {{...}} 块。

Jinja2 模板同样支持控制语句，像在 {%...%} 块中。
'''

