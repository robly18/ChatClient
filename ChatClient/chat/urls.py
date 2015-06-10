from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<roomName>[a-zA-Z0-9_]+)', views.chatroom, name='chatroom'),
]