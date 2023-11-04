import json

from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Room, Message

# import threading

class ChatConsumer(AsyncWebsocketConsumer):
    #function of connecting to the server

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"
        # self.room_group_name = 'chat_%s' % self.room_name

        #join roomname and room group name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # to get the thread id
        # print(threading.get_native_id())

        await self.accept()
        #after this we are authenticated and connected to the server 




    #function of disconnecting the server
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )




    #right code to receive message from websocket
    async def receive(self, text_data):
        # Parse the received JSON message
        message = json.loads(text_data)

        # Extract the message type from the parsed message
        message_type = message['type']

        message_text = message['message']
        message_username = message['username']
        message_room = message['room']

        # Handle different message types
        if message_type == 'chat-message':
            # Handle the chat message
            # await self.handle_chat_message(message)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    # 'type': 'chat.message',(both will work)
                    'message': message_text,
                    'username':message_username,
                    # 'room':message_room
                }
            )

            

            await self.save_message(message_username,message_room,message_text)
        else:
            # Handle other message types or raise an error
            raise ValueError(f"No handler for message type {message_type}")

    #chat_message part
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        # print(event) #it will be printed n times cause it will be sent to all the channels(users) in the group if there is n number of user or channel in the group.

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username':username
        }))
        




    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)


        Message.objects.create(user=user, room=room, content=message)

    




