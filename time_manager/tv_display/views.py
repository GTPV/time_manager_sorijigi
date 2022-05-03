from channels.layers import get_channel_layer
from django.shortcuts import render
from .consumers import TvConsumer
from time_manage.models import *
from asgiref.sync import async_to_sync
from django.conf import settings

# Create your views here.
def index(response):
    return render(response, 'tv_display/tv.html', {})

def update_music(response, _u_i, _music_id):
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
            'type' : 'update_tv',
            'update_type' : 'music',
            'info' : _music_info_dict,
        },
    )

def update_breaktime(response, _time_start, _time_end):
    _breaktime_info_dict = {
        "time_start" : _time_start,
        "time_end" : _time_end,
    }
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        settings.STREAM_SOCKET_GROUP_NAME,
        {
            'type' : 'update_tv',
            'update_type' : "breaktime",
            'info' : _breaktime_info_dict,
        },
    )