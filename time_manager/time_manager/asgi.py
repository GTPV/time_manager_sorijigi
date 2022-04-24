"""
ASGI config for time_manager project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from tv_display import routing as tv_display_routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'time_manager.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    "websocket":AuthMiddlewareStack(
        URLRouter(
            tv_display_routing.websocket_urlpatterns
        )
    ),
})
