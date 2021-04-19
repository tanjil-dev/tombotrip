"""
ASGI config for tombitrip project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from django.core.asgi import get_asgi_application

from home.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tombitrip.settings')

application = get_asgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    # url(r"messages/(?P<username>[\w.@+-]+)/$", ChatConsumer, name='chat')
                ]
            )
        )
    )
})