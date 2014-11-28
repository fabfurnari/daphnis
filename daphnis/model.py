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
    feeds = db.relationship('Feed',backref='author',lazy='dynamic')

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

tagmap = db.Table('tagmap', db.Model.metadata,
    db.Column('tag_id',db.Integer, db.ForeignKey('tag.id')),
    db.Column('feed_id', db.Integer, db.ForeignKey('feed.id'))
    )
    
class Feed(db.Model):
    __tablename__ = 'feed'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True)
    url = db.Column(db.String(200), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tags = db.relationship('Tag', secondary=tagmap,
                           backref='feeds')
    entries = db.relationship('Entry', backref='site',lazy='dynamic')

    def __init__(self, title, url, tags, user_id):
        self.title = title
        self.url = url
        self.tags = tags
        self.user_id = user_id
        
    def __repr__(self):
        return '<Feed %r>' % self.title


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
    summary = db.Column(db.Text)
    description = db.Column(db.Text)
    link = db.Column(db.String(200))
    pub_date = db.Column(db.DateTime)
    parse_date = db.Column(db.DateTime)
    feed_id = db.Column(db.ForeignKey('feed.id'))

    def __init__(self,
                 title,
                 summary,
                 description,
                 link,
                 pub_date,
                 parse_date,
                 feed_id):
        self.title = title
        self.summary = summary
        self.description = description
        self.link = link
        self.pub_date = pub_date
        self.parse_date = parse_date
        self.feed_id = feed_id

    def __repr__(self):
        return '<Entry %r>' % self.title

