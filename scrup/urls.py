from django.conf.urls.defaults import *

urlpatterns = patterns('scrup.views',
    url(r'upload/((?P<filename>.+?)/?)?$', 'upload', name='upload'),
)