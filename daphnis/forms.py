from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField, HiddenField
from wtforms.validators import Required, Length, EqualTo, Email, URL, Optional

from daphnis.model import User
from daphnis import db

class LoginForm(Form):
    username = TextField(u'Username', [Required()])
    password = PasswordField(u'Password', [Required()])
    remember_me = BooleanField(u'Remember me')

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(
            username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True

class RegisterForm(Form):
    """
    Maybe a real email validation here
    """
    username = TextField(u'Username',[Required(),Length(min=4,max=15)])
    password = PasswordField(u'Password',[Required(),Length(min=6,max=25)])
    r_password = PasswordField(u'Repeat Password',[Required(),
                                                  EqualTo('password', message='password mismatch')])
    email = TextField(u'Email address',[Required(),Email(message='Malformed email')])
    accept_tos = BooleanField(u'I accept the Terms of Service', [Required()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        check_user = User.query.filter_by(username=self.username.data).first()
        check_email = User.query.filter_by(email=self.email.data).first()
        if check_user:
            self.username.errors.append('Username already taken')
            return False
        elif check_email:
            self.email.errors.append('This email address has already been used!')
            return False
        else:
            u = User(self.username.data,
                     self.email.data,
                     self.password.data)
            db.session.add(u)
            db.session.commit()

        return True
