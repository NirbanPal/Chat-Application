from django.core.management.base import BaseCommand
from django.utils import timezone 
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync 

# While using inMemoryChannelayer(for testing, development piurpose not for production) we won't be able to use this notification system. We can use this only in redis(memurai) or rabbit mq etc. 
# we can also run this command from the celery also
class Command(BaseCommand):
    help='Displays current time'

    def handle(self,*args,**kwargs):
        channel_layer = get_channel_layer()
        print("hello")
        async_to_sync(channel_layer.group_send)("chat_hobby",{
            'type':'chat_message',
            'message':'notofications',
        })