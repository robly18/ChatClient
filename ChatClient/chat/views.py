from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def chatRoom(request, roomName):
	return render(request, "chat/chatRoom.html", {'roomName':roomName})

def msgInput(request):
	print("Got a message input!!!")
	print(request.POST['msgInput'])
	pass
