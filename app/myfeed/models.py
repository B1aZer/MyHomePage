from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.encoding import smart_str, smart_unicode
import datetime



class System(models.Model):
    #user =  models.ForeignKey(User)
    title = models.CharField( max_length = 255)
    active = models.BooleanField(default = True)
    
    def __unicode__(self):
        return self.title

class Member(models.Model):  
    system = models.ForeignKey(System)  
    sysid = models.CharField( max_length = 255, blank = True)
    nick = models.SlugField(blank = True)
    name = models.CharField( max_length = 255, blank = True)
    link = models.CharField( max_length = 255, blank = True)
    picurl = models.CharField( max_length = 255, blank = True)
    text = models.TextField(blank = True)

    def __str__(self):  
          return smart_str("%s's profile" % self.nick)

class Message(models.Model):
    user = models.ForeignKey(Member)
    system = models.ForeignKey(System)
    title = models.SlugField(blank = True)
    mesid = models.CharField( max_length = 255, blank = True)
    link = models.CharField( max_length = 255, blank = True)
    text = models.TextField(blank = True)
    read = models.BooleanField(default = False)
    updated = models.DateField(auto_now = True)
    attach = models.TextField(blank = True)
    created = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.text
    
#    class Meta:
#        unique_together = ("system", "text")


