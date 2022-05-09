from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#now import the views.py file into this code
from .views import *
urlpatterns=[
    path('',index),
    path('netflix',netflix),
    path("dropbox",dropbox),
    path("snapchat",snapchat),
    path("github",github),
    path("facebook",facebook_mobile),]

urlpatterns += staticfiles_urlpatterns()
