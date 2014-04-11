from django.conf.urls import patterns, include, url
from rff.views import rff
from parser import main


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'runforfun.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rff/$', rff.run_parser),
)
