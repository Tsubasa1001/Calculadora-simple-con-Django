from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^prefix/$', views.prefix, name="prefix"),
    url(r'^postfix/$', views.postfix, name="postfix"), 
    url(r'^tree/$', views.tree, name="tree"),
]
