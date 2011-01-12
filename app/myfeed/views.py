# -*- coding: utf-8 -*-
#from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response,get_object_or_404
import twitter
import logging
import facebook
import datetime
import urllib2,urllib,cookielib
import re
from BeautifulSoup import BeautifulSoup,Tag
from time import clock,localtime
from app.myfeed.models import *
import os.path
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from soupselect import select
#test
from django.db import connection


COOKIEFILE = 'cookie'
FEED_COUNT = 5

class Person:
    def __init__(self):
        self.url=None
        self.name=None
        self.nick=None
        self.image=None
    def add(self,**kwargs):
        logging.debug(kwargs)
        #self.url = kwargs['url']
        #self.nick = kwargs['nick']
        #self.image = kwargs['image']
        #[self.key = kwargs[key] for key in kwargs]
        for key in kwargs:
            setattr(self, key, kwargs[key])
            #logging.debug(self.key)
def sql_debug():
    #offset = len(connection.queries)
    #print("wtf")
    #print("offset",offset)
    #conn = connection.queries[offset:]
    #conn = connection.queries
    #print(conn)
    #queries = connection.queries[offset:]
    queries = connection.queries
    sum_time = sum([q['time'] for q in queries])
    #sql_time = [(q['time'],q['sql']) for q in queries]
    sql_time = ["%s=%s" % (q['time'],q['sql']) for q in queries]
    sql_time = "\n".join(sql_time)
    print(sql_time)
    print(sum_time)



def load_from_db(systitle, FEED_C = 5):
    try: 
        #data = {}
        #system = System.objects.get(title = systitle)
        #users = system.member_set.all()
        #for user in users:
            #user.message_set.all()
        #print("user",users[0])
        messages = Message.objects.select_related().filter( system__title = systitle ).order_by('-created')[:FEED_C]
    except:
        pass
    return messages


def save_to_db(data, user, systitle='Vkontakte'):
    #logging.debug(type(da ta))
    if isinstance(data, list):
        if user.is_authenticated():
            system, created = System.objects.get_or_create( title = systitle, user = user)
        else:
            system = System.objects.get( title = systitle)
        try:
            mes1 = data[0]['message']
            exist = system.message_set.filter(text__contains = mes1)
        except:
            logging.debug('Vkontakte Parse Error') 
            exist = None

        if not exist:
            for status in data:
                #for status in persons:
                    try:
                        #logging.debug(status['date'])
                        #date = localtime(float(status['date']))
                        date = datetime.datetime.fromtimestamp(float(status['date']))
                        #date = strftime("%a %b %y %H:%M:%S +0000 %Y",date)
                                        #+ datetime.timedelta(hours=3)
                        #logging.debug(type(date))
                        m, created = Member.objects.get_or_create(system = system, \
                                name = status['name'], \
                                sysid = status['link'], \
                                nick = status['nick'], \
                                picurl = status['image'], \
                                #text = status['text'] \
                                )
                        s = Message(user = m, \
                            system = system, \
                            #mesid = status["id"], \
                            link = status["link"], \
                            text = status["message"], \
                            created = date,
                            )
                        s.save()
                    except:
                        #pass
                        logging.debug('not unique Vkontakte message - aint saving')




def parser(data):
    list_stats = []
    soup =  BeautifulSoup(data)
    content = soup.prettify()
    #content = soup.find('div', id = 'feed_rows')
    #parsed = {}
    #length = len(soup.findAll('a', { "class" : "post_image fl_l" }))
    #images = [tag['image'] for tag in soup.findAll('a', { "class" : "post_image fl_l" })]
    #urls = ["tag['href'] = %s" % (tag) for tag in soup.findAll('a')]
    #urls = dict([dict(['href',hr]) for hr in ['1','2','3','4']])
    #a={}
    #for hr in ['1','2','3','4']:
    #    urls = a.append((dict(hr = 'href')))
    #parsed["name"] = soup.find('a', { "class" : "author fl_l" }).string
    #parsed["image"] = soup.find('a', { "class" : "post_image fl_l" }).img["src"]
    #parsed["message"] = soup.find('div', {"class" : 'text'})
    #parsed["date"] = soup.find('span', {"class" : 'rel_date'})#.string.decode('utf-8')
    #parsed["link"] = soup.find('a', { "class" : "author fl_l" })["href"]
    
    #for person in soup.find('div', id = 'feed_rows').find('a','author'):
        #name = person
        #name = person.find('a','author')
        #name = select(person,'a.post_image')
        #logging.debug(person) 
    
    
    
    for person in select(soup,'div#feed_rows'):
        #names = ''
        #links = ''
        #images = ''
        #messages = ''
        #dates = ''
        nick = ''
        statuses = {}
        list_stats = []
        #ii=1
        #logging.debug(person)
        #image = select(person,".post_image")
        #images = select(person,".post_image")
        for i in person:
            if isinstance(i, Tag):
                #name = i.find('a', { "class" : "author fl_l" })
                pattern = re.compile(u'[^a-zA-Z0-9_а-яА-Я] ',re.UNICODE)
                name = str(i.find('a', { "class" : "author fl_l" }).string).decode('utf-8','ignore').strip()
                name = re.sub(pattern,'',name)
                if name:
                    statuses['name'] = name
                image = i.find('a', { "class" : "post_image fl_l" }).img["src"]
                if image:
                    statuses['image'] = image
                message = i.find('div', 'text').contents[1]
                if message:
                    statuses['message'] = message
                date = i.find('span', {"class" : 'rel_date rel_date_needs_update'})#.string.decode('utf-8')
                #logging.debug(person)
                if date:
                    #date = i.find('span', {"class" : 'rel_date'}).contents[0]
                    #logging.debug(date['time'])
                    statuses['date'] = date['time']
                link = i.find('a', { "class" : "author fl_l" })["href"]
                if link:
                    statuses['link'] = link
                    nick = link.replace('/','')
                    statuses['nick'] = nick
                #print(statuses)
                #logging.debug(nick)
                list_stats.append(dict(statuses))
                #list_stats = sum(list_stats,statuses)
                #print(list_stats)
                #ii +=1
                #if ii == 3: break
    #logging.debug("\n".join(["%s = %s" % ["k,v" for k,v in lister] for lister in list_stats]))
    #f = open('file.txt','w')
    #list_stats = [["\n".join('%s === %s\t' % (k,v) for k,v in lister.items())] for lister in list_stats]
    #f.write(str(list_stats))
    #f.close()
    #logging.debug(list_stats) 
    return content, list_stats

def browser(url, post = None):
    cookies =  cookielib.LWPCookieJar()
    if os.path.isfile(COOKIEFILE):
        # if we have a cookie file already saved
        # then load the cookies into the Cookie Jar
        cookies.load(COOKIEFILE)
        logging.debug('load cooky') 
    if post:
        post = urllib.urlencode(post)
        request = urllib2.Request(url, post)
        logging.debug('posting')
    else:
        request = urllib2.Request(url)
    cookie_handler= urllib2.HTTPCookieProcessor( cookies )
    #redirect_handler= urllib2.HTTPRedirectHandler()
    #opener = urllib2.build_opener(redirect_handler,cookie_handler)
    opener = urllib2.build_opener(cookie_handler)
    handle = opener.open(request)
    data = handle.read()
    #if cookies is None:
    #    logging.debug('no cooky for today')
    #else:
    cookies.save(COOKIEFILE)
    handle.close()
    return data


def vk_feed(user):
    post  =  {
    'email' : '2bbf@mail.ru',
    'from_host' : 'vkontakte.ru',
    'pass' : 'armanda666',
    'act' : 'login',
    'q' : '1',
    'al_frame' : '1'
    }
    url='http://login.vk.com/?act=login'
    url2='http://vkontakte.ru/feed'
    #fopen = open('test.html','w')
#TEST
    #fl = open('test.html')
    data = browser(url2)
    #fopen.write(data)
    #fopen.close()
    #data = fl.read()
    content, lister = parser(data)
    #data.encode('cp1251')#.encode('utf-8')
    #content = new_parser(data)
    #logging.debug("new parsing")
    #load_from_db()
    #fl.close()
    if not lister:
        browser(url,post)
        data = browser(url2)
        content, lister = parser(data)
        save_to_db(lister,user)
    else:
        save_to_db(lister,user)
    return content

def fb_feed(user):
    FACEBOOK_APP_ID = "184062098289427"
    FACEBOOK_APP_SECRET = "75fb6b2dadcfb90c3b4da7f7593d439b"
    FACEBOOK_OATH_TOKEN = "184062098289427|581fb9c8dabc8880f5114c1a-586527073|qZ5xs_S2_rwvaYsLXdXKZVwcST8"
    try:
        graph = facebook.GraphAPI(FACEBOOK_OATH_TOKEN)
        news_feed = graph.get_connections("me", "home")
    except:
        logging.debug("error auth from fb")
        news_feed = {}
    if user.is_authenticated():
        system, created = System.objects.get_or_create( title = 'Facebook', user = user)
    else:
        system = System.objects.get( title = 'Facebook')

    #print(news_feed["data"])
    #system = get_object_or_404(System.objects,title__contains = 'Twitter')
    try:
        exist = system.message_set.filter(text__contains = news_feed["data"][0]["message"])
    except:
        logging.debug('Twitter Api Error') 
        exist = None
    #logging.debug('exist' + str(exist))
    if not exist:
        for status in news_feed["data"]:
                try:
                    date = datetime.datetime.strptime( \
                                    status["created_time"], "%Y-%m-%dT%H:%M:%S+0000") + \
                                    datetime.timedelta(hours=3)
                    #logging.debug(str(date))
                    m, created = Member.objects.get_or_create(system = system, \
                            name = status["from"]["name"], \
                            sysid = status["from"]["id"], \
                            nick = status["from"]["name"])
                    s = Message(user = m, \
                        system = system, \
                        text = status["message"], \
                        created = date)
                    s.save()
                except:
                    logging.debug('not unique Facebook message - aint saving')
#Delete
    #if news_feed:
    #    for post in news_feed["data"]:
    #        post["created_time"] = datetime.datetime.strptime(
    #            post["created_time"], "%Y-%m-%dT%H:%M:%S+0000") + \
    #            datetime.timedelta(hours=3)
    return news_feed

def tw_feed(user):
 
    userName = 'b1azer'
    password = 'armanda'
    statuses = {}

    if userName is not None and password is not None:
        try:
            api = twitter.Api(
                consumer_key='2yoD9AScEFJWIVI6lc6Nmg',
                consumer_secret='qf2Pi3qsHvA0RjomsnNRhY5iKDWHIVy9DQWGBzDQIkw', 
                access_token_key='41890375-8WtfwO4GnEp0Gv2ewt9XfGVmaSoayNYpmn2JhtTb9', 
                access_token_secret='fXeT4By3y15b8jZT1IkDPRQNnFEL507wxgsJGVSVrvo') 
            statuses = api.GetFriendsTimeline('b1azer')[:FEED_COUNT]
            #system = System.objects.get(title = 'Twitter')
            if user.is_authenticated():
                system, created = System.objects.get_or_create( title = 'Twitter', user = user)
            else:
                system = System.objects.get( title = 'Twitter')
            #system = get_object_or_404(System.objects,title__contains = 'Twitter')
            try:
                exist = system.message_set.filter(text__contains = statuses[0].text)
            except:
                logging.debug('Twitter Api Error') 
            #logging.debug('exist' + str(exist))
            if not exist:
                for status in statuses:
                    try:
                        date = datetime.datetime.strptime( \
                                        status.created_at, "%a %b %d %H:%M:%S +0000 %Y") + \
                                        datetime.timedelta(hours=3)
                        #logging.debug(str(status.created_at))
                        #logging.debug(str(date))
                        m, created = Member.objects.get_or_create(system = system, \
                                name = status.user.name, \
                                sysid = status.user.id, \
                                nick = status.user.screen_name, \
                                picurl = status.user.profile_image_url, \
                                text = status.user.description)
                        s = Message(user = m, \
                            system = system, \
                            mesid = status.id, \
                            link = status.source, \
                            text = status.text, \
                            created = date)
                        s.save()
                    except:
                        logging.debug('not unique Twitter message - aint saving')

        except NameError, e:
            logging.debug('unable to login: ' + str(e))

    else:
        statuses = {}
    return statuses

class SocialAnalisator:
    def __init__(self):
        self.marks = {}
        logging.debug('class init')
    def loadsystem(self, ufo):
        logging.debug('loading')
        if isinstance(ufo, list):
            logging.debug('checking'+str(ufo))
            if [elem for elem in ufo]:
                logging.debug()
        else:
            logging.debug('not found')


def index(request):
    template = 'base.html'
    if request.method == 'POST':
        userName = request.POST.get( 'userTxt' )
        password = request.POST.get( 'passwordTxt' )
    #messages = statuses.objects.all()
    #logging.debug(messages)
    start = clock()
    fb_news  = {}
    vk_news = {}
    tw_news = {}
    #p = Person()
    #p.add(url = 'http://')
    #logging.debug(p.url)

    fb_news = fb_feed(request.user) #~0.05
    fb_news = load_from_db('Facebook')
    vk_news = vk_feed(request.user) #~1.0 with cooky 1.17 without
    vk_news = load_from_db('Vkontakte')
    tw_news = tw_feed(request.user) #~0.09 with db
    tw_news = load_from_db('Twitter')
    #s = SocialAnalisator()
    #s.loadsystem(tw_news)
    elapsed = (clock() - start)
    logging.debug(elapsed)
    #sql_debug()
    #logging.debug(vk_news[0].message_set.)
    variables = RequestContext(request, {
    #variables = {
        #'show_edit': username == request.user.username,
        'tw_news' : tw_news,
        'hello' : 'hello',
        'news_feed' : fb_news,
        'vk_news' : vk_news,
        'page_title' : 'My Home Page',
        'head_title' : 'MyHomePage',
      })
    #context_instance=RequestContext(request)
    #print(variables)
    return render_to_response(template, variables)
    #return render_to_response(template,
    #                          variables,
    #                          context_instance=RequestContext(request))
