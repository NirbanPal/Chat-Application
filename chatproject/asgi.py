"""
ASGI config for chatproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

#extra stuffs for the router.py and consumers.py
import os

from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatproject.settings')

import django
django.setup()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter


from rooms.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})



#here we are using AuthMiddlewareStack so that we can use authentication middleware of django. We can populate request like request.user (so that we actually can populate user attribute in request object)field. As we have created authentication features like login,logout,signup etc that user can login first and then chat.That is why AuthMiddlewareStack we are using. as we use request.user in django so for the websocket we have to use self.scope['user'] to parse the user
