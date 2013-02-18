from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'bookmark.views.index'),
    url(r'^tag/(?P<slug>\w+)/$', 'bookmark.views.tag_bookmarks', name='tag_bookmarks'),
    url(r'^bookmark/(?P<pk>\d+)/deactivate/$', 'bookmark.views.deactivate_bookmark', name='deactivate_bookmark'),
    
)
