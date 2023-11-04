from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse

from .models import *
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync 

# Create your views here.

@login_required
def rooms(request):
    rooms=Room.objects.all()
    return render(request,'rooms/rooms.html',{'rooms':rooms})

@login_required
def room(request,slug):
    room=Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)
   

    return render(request, 'rooms/room.html', {'room': room, 'messages': messages})


# # In this way Notification is sent. We have to work on it also. As we have created a notify.py in management\commands. if we run that code (py manage.py notify) notification will be sent to that group. We also can use celery to automate the process.  
# async def send_noti(slug):
#     r_name=f"chat_{slug}"
#     #notification
#     channel_layer = get_channel_layer()
#     await channel_layer.group_send(r_name,{
#             'type':'chat_message',
#             'message':'Conversation started(Notification)',
#         })
    
#     return HttpResponse("Done")