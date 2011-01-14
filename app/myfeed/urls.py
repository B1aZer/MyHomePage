from django.conf.urls.defaults import *
from app.myfeed.views import *

#info_dict = {
#    'queryset': Twitme.objects.all()
#}

urlpatterns = patterns('',
    #(r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^$', index),
    #(r'test', index_all),
)
