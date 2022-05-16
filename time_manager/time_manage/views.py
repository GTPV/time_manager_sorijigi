from django.core.exceptions import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from tv_display import views as tv_display_views

# Create your views here.
def index(response):
    return redirect('/time_manage/list')

def create(response):
    _time_create_form = CreateNewTime()
    _var = {"time_create_form" : _time_create_form}
    if response.method == "POST":
        _time_create_form = CreateNewTime(response.POST)

        if _time_create_form.is_valid():
            _time_create_form.save()
            return redirect("../")
        else:
            print(f'form is not valid')
            return HttpResponse("""form is invalid  <a href='./'>resubmit</a>""")

        return HttpResponseRedirect("./")
    else:
        _time_create_form = CreateNewTime()
    return render(response, 'time_manage/create.html', _var)

def list(response):
    _var = {"time_info" : TimeInfo.objects.all()}
    if response.method =="POST":
        if response.POST.get("filter_time_by_date"):
            _form = FilterTime(response.POST)
            if _form.is_valid():
                _time_date= _form.cleaned_data["_time_date"]
                _var["time_info"] = TimeInfo.objects.filter(time_date=_time_date)
                return render(response, 'time_manage/list.html', _var)
            else:
                print(f'\n\nform is not valid\n\n')
        else:
            print(f'\n\nresponse method is POST, {response.POST}\n\n')
    else:
        print(f'\n\nresponse method is not POST\n\n')
    return render(response, 'time_manage/list.html', _var)

def manage(response, _u_i):
    _time_info = TimeInfo.objects.get(time_unique_id = _u_i)
    _music_add_form = AddMusic()
    _player_list_form = AddPlayer()
    _var = {"time_info" : _time_info, "music_add_form" : _music_add_form, "player_list_form" : _player_list_form}

    if response.method == "POST":
        if response.POST.get("add_music"):
            _music_add_form = AddMusic(response.POST)
            _player_list_form = AddPlayer(response.POST)
            _player_list = []
            if _music_add_form.is_valid() and _player_list_form.is_valid():
                print('\n\nform_is_valid\n\n')
                #_time_info.music_set.create(**_music_add_form.cleaned_data)
                _music_info = Music(**_music_add_form.cleaned_data)
                _music_info.time_info = _time_info
                _music_info.save()
                _player_list = [i.strip() for i in _player_list_form.cleaned_data["_player_list"].split(sep=',')]
                print(f'\n\nplayer list : {_player_list}\n\n')
                if len(_player_list) > 0:
                    for _p_i in _player_list:
                        _player_info = [i.strip() for i in _p_i.split(sep=":")]
                        print(f'\nplayer_info : {_player_info} \n')
                        if len(_player_info) == 2:
                            player_info = Player(player_name = _player_info[1], player_instrument = _player_info[0], music = _music_info)
                            player_info.save()
                return redirect("./")
            print('\nform is not valid\n')
        elif response.POST.get("update_tv_breaktime"):
            _breaktime_form = UpdateBreaktime(response.POST)
            if _breaktime_form.is_valid():
                update_tv_breaktime(response, _breaktime_form.cleaned_data["_time_start"], _breaktime_form.cleaned_data["_time_end"])
            return redirect("./")
        else:
            print('\nresponse is not (add_music or update_tv_breaktime)\n')
            _music_add_form = AddMusic()
    return render(response, 'time_manage/manage.html', _var)

def delete_music(response, _u_i, _music_id):
    _music_info = Music.objects.get(id = _music_id)
    _music_info.delete()
    return redirect(f'/time_manage/{_u_i}/')

def insta_upload(response, _u_i):
    _var = {"time_info" : TimeInfo.objects.get(time_unique_id=_u_i)}
    return render(response, 'time_manage/instagramupload.html', _var)

def update_tv_music(response, _u_i, _music_id):
    tv_display_views.update_music(response, _u_i, _music_id)
    return redirect(f'/time_manage/{_u_i}/')

def update_tv_breaktime(response, _time_start, _time_end):
    tv_display_views.update_breaktime(response, _time_start, _time_end)
    return None