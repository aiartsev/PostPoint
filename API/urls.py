__author__ = 'Alex'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from API import views

urlpatterns = [
    url(r'^posts/$', views.post_list),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.post_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)