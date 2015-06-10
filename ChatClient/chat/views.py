from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def chatRoom(request, roomName):
	return render(request, "chat/chatRoom.html")

def msgInput(request):
	pass
