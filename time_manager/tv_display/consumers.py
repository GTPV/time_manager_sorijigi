import json
from channels.generic.websocket import AsyncWebsocketConsumer
from time_manage.models import Music
from django.conf import settings

class TvConsumer(AsyncWebsocketConsumer):
    group_name = settings.STREAM_SOCKET_GROUP_NAME

    async def connect(self):
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)

        await self.channel_layer.group_send({
            self.group_name,
            {
                'type' : 'update_music',
                'data' : {
                    'music_composer' : "작곡가",
                    'music_title' : "곡 제목",
                    'music_orchestra' : "오케스트라",
                    'music_conductor' : "지휘자",
                },
            },
        })

    async def update_music(self, event):
        print("update_music called!!")
        await self.send(text_data=json.dumps(event['data']))