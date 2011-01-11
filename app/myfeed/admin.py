from app.myfeed.models import System, Message, Member
from django.contrib import admin

class MessageAdmin(admin.ModelAdmin):
    list_display = ['id','text','user','system']
    #list_editable = ['active']

class MemberAdmin(admin.ModelAdmin):
    list_display = ['id','name','system']
    #list_editable = ['active']

admin.site.register(System)
admin.site.register(Message,MessageAdmin)
admin.site.register(Member,MemberAdmin)
