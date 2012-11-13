# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns("gamified.badges.views",
   url(r'^$', "badge_list", name="badge_list"),
   url(r'^for/(?P<username>[^/]+)/$', "user_badges", name="user_badges"),
   )
