import json
from channels.generic.websocket import AsyncWebsocketConsumer
from time_manage.models import Music

class TvConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        pass

    async def disconnect(self):
        pass

    async def receive(self, _music_id):
        _music_info = Music.objects.get(id=_music_id)
        pass