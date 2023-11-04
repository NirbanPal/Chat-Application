#we have a file urls.py for for our different pages we want similar file for the web socket(here we are creating routing.py for this)

from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]
