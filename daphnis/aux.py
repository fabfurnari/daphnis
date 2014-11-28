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
    Creates an entry. If tag does not exists creates the tag
    too.
    TODO:
    * check duplicate entries (?)
    '''
    tag_list = []
    for tag in tags.split(','):
        t = Tag.query.filter(Tag.name.like(tag)).first()
        if not t:
            t = Tag(name=tag.lower())
            db.session.add(t)
        tag_list.append(t)
        
    f = Feed(title=title,url=url,tags=tag_list,user_id=user_id)
    db.session.add(f)
    db.session.commit()
    
