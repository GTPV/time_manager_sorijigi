from channels.layers import get_channel_layer
from django.shortcuts import render
from .consumers import TvConsumer
from time_manage.models import *
from asgiref.sync import async_to_sync
from django.conf import settings

# Create your views here.
def index(response):
    return render(response, 'tv_display/tv.html', {})

def update(response, _u_i, _music_id):
    print('tv_display.views.update called!!')
    _music_info = Music.objects.get(id=_music_id)
    _music_info_dict = {
                "music_composer": _music_info.music_composer,
                "music_title": _music_info.music_title,
                "music_orchestra": _music_info.music_orchestra,
                "music_conductor": _music_info.music_conductor,
    }
    print('_music_info_dict : ' + str(_music_info_dict))
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        settings.STREAM_SOCKET_GROUP_NAME,
        {
            'type' : 'update_music',
            'data' : _music_info_dict,
        },
    )