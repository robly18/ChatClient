from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def chatroom(request, roomName):
	return HttpResponse("hello you are in chatroom %s" % roomName)
