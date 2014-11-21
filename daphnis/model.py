from daphnis import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    registered_on = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.username

tags = db.Table('tags',
    db.Column('tag_id',db.Integer, db.ForeignKey('tag.id')),
    db.Column('feed_id', db.Integer, db.ForeignKey('feed.id'))
    )
    
class Feed(db.Model):
    __tablename__ = 'feed'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True)
    url = db.Column(db.String(200), unique=True)
    tags = db.relationship('Tag', secondary=tags,
                           backref=db.backref('feeds', lazy='dynamic'))

    def __init__(self, title, url):
        self.title = title
        self.url = url

    def __repr__(self):
        return '<Feed %r' % self.title


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tag %r>' % self.name

    
class Entry(db.Model):
    __tablename__ = 'entry'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.Text)
    link = db.Column(db.String(200))
    pubdate = db.Column(db.DateTime)

    def __init__(self, title, description, link, pubdate):
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def __repr__(self):
        return '<Entry %r>' % self.title

