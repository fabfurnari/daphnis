from daphnis import db
from daphnis.model import *

def a_show_feeds(user=None):
    '''
    Return all feeds for a given user as list of
    dicts that can be easily parsed by frontend
    '''
    # checks here
    u = User.query.filter_by(username=user).first()
    if u:
        r = []
        for feed in u.feeds:
            d = dict()
            d['title'] = feed.title
            d['url'] = feed.url
            d['tags'] = [ t.name for t in feed.tags ]
            r.append(d)

        return r
    else:
        return None

def a_add_feed(title,url,tags,user_id):
    '''
    '''
    f = Feed(title=title,url=url,tags=tags,user_id=user_id)
    db.session.add(f)
    db.session.commit()
    
