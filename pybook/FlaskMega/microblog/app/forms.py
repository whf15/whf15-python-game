# from flask.ext.wtf import Form 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()]) 
    password = PasswordField('Password', validators=[DataRequired()]) 
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    # openid = StringField('openid', validators=[DataRequired()])
    # remember_me = BooleanField('remember_me', default=False)

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    # email在DataRequired之后添加了第二个验证码
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    # 使用EqualTo验证器，确保与第一个password字段的值相同
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


# 当添加validate_<file_name>的方法时，WTForms将这些方法作为自定义验证器

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address!')