from django.conf.urls.defaults import patterns, include, url
from blog.core.views import PostsView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', PostsView.as_view()),

    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
