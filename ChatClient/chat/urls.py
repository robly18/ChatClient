from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^room/(?P<roomName>[a-zA-Z0-9_]+)/$', views.chatRoom, name='chatRoom'),
    ]
