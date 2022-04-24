from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/tv_display/$', consumers.TvConsumer.as_asgi()),
]