from flask import request, g, render_template, flash, redirect, url_for
from flask.ext.login import LoginManager, login_user, \
     logout_user, current_user, login_required
     
from daphnis import app, db
from daphnis.model import *
from daphnis.forms import *
from daphnis.aux import *

# login and logout

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html',form=form)
    if form.validate_on_submit():
        flash('User successfully registered')
        return redirect(url_for('login'))
    else:
        return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    remember_me = False
    form = LoginForm()
    if form.validate_on_submit():
        if form.remember_me.data:
            remember_me = True
        login_user(form.user, remember=remember_me)
        flash('Successfully logged in as %s' % form.user.username)
        return redirect(request.args.get('next') or url_for('index'))
    return render_template('login.html',form=form)
        
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# end login and logout

# start main views

@app.route('/')
def index():
    form = AddFeedForm()
    if current_user.is_authenticated():
        feeds = a_show_feeds(user=g.user.username)
    else:
        feeds = []
    return render_template('index.html',
                           form=form,
                           feeds=feeds)

@app.route('/user/<username>')
def profile(username):
    return NotImplementedError

@login_required
@app.route('/add', methods=['POST'])
def add_feed():
    a_add_feed(title=request.form['title'],
               url=request.form['url'],
               tags=request.form['tags'],
               user_id=g.user.id)
    return redirect(url_for('index'))
    
# end main views
