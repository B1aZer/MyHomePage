from django.conf.urls.defaults import *
from django.conf import settings
from app.myfeed.views import *
#from utils.json_dec import json_view

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^homepage/', include('homepage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', include('app.myfeed.urls')),
    (r'^test/', index_all),
    (r'^json/', json_all),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
         'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        }),
    )
