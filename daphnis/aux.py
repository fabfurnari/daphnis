from daphnis import db
from daphnis.model import Tag, User, Feed, Entry
import feedparser
from threading import *
import copy

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
            d['id'] = feed.id
            d['title'] = feed.title
            d['url'] = feed.url
            d['tags'] = [ t.name for t in feed.tags ]
            r.append(d)

        return r
    else:
        return None

def a_add_feed(title,url,tags,author):
    '''
    Creates an entry. If tag does not exists creates the tag
    too
    '''
    tag_list = []
    for tag in tags.split(','):
        t = Tag.query.filter(Tag.name.like(tag)).first()
        if not t:
            t = Tag(name=tag.lower())
            db.session.add(t)
        tag_list.append(t)
        
    f = Feed(title=title,url=url,tags=tag_list,author=author)
    db.session.add(f)
    db.session.commit()

def parse_feed(user=None):
    '''
    Parses a list of feeds for a given user and put relevant
    values into the entries table
    '''
    u = User.query.filter_by(username=user).first()
    url_list = [x.url for x in u.feeds]
    async_calls = [Future(feedparser.parse,rss_url) for rss_url in url_list]
    # this contains the whole feed list
    feeds = [f_obj() for f_obj in async_calls]
    for feed in feeds:
        # horrible
        f = Feed.query.filter_by(url=feed['url']).first()
        for item in feed['item']:
            e = Entry(title=item['title'],
                      summary=item['summary'],
                      link=item['link'],
                      pub_date=item['date'],
                      parse_date=item['date_parsed'],
                      feed_id = f.id)
            db.session.add(e)
    db.commit()
            
class Future:
    def __init__(self,func,*param):
        # Constructor
        self.__done=0
        self.__result=None
        self.__status='working'

        self.__C=Condition()   # Notify on this Condition when result is ready

        # Run the actual function in a separate thread
        self.__T=Thread(target=self.Wrapper,args=(func,param))
        self.__T.setName("FutureThread")
        self.__T.start()

    def __repr__(self):
        return '<Future at '+hex(id(self))+':'+self.__status+'>'

    def __call__(self):
        self.__C.acquire()
        while self.__done==0:
            self.__C.wait()
        self.__C.release()
        # We deepcopy __result to prevent accidental tampering with it.
        a=copy.deepcopy(self.__result)
        return a

    def Wrapper(self, func, param):
        # Run the actual function, and let us housekeep around it
        self.__C.acquire()
        try:
            self.__result=func(*param)
        except:
            self.__result="Exception raised within Future"
        self.__done=1
        self.__status=`self.__result`
        self.__C.notify()
        self.__C.release()
