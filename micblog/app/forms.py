# -*- coding:utf-8 -*-


from flask_wtf import FlaskForm
from wtforms import TextField,BooleanField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import Required,Email,Length

class LoginForm(FlaskForm):
	user_name = TextField('User Name', validators = [Required(),Length(max = 15)])
	#password = PasswordField('Password', validators = [Required()])
	remember_me = BooleanField('Remember_me', default = False)
	submit = SubmitField('Log in')


class SignUpForm(FlaskForm):
    user_name = TextField('user name', validators = [Required(), Length(max=15)])
    user_email = TextField('user email', validators = [Email(), Required(), Length(max=128)])
    submit = SubmitField('Sign up')

class AboutMeForm(FlaskForm):
    describe = TextAreaField('about me', validators = [Required(), Length(max=140)])
    submit = SubmitField('YES!')

class PublishBlogForm(FlaskForm):
	body = TextAreaField('blog content', validators = [Required()])
	submit = SubmitField('Submit')	