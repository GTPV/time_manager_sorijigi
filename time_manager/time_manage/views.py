from django.core.exceptions import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from tv_display import views as tv_display_views

# Create your views here.
def index(request):
    return redirect('/time_manage/list')

def create(request):
    _time_create_form = CreateNewTime()
    _var = {"time_create_form" : _time_create_form}
    if request.method == "POST":
        _time_create_form = CreateNewTime(request.POST)

        if _time_create_form.is_valid():
            _time_create_form.save()
            return redirect("../")
        else:
            print(f'form is not valid')
            return HttpResponse("""form is invalid  <a href='./'>resubmit</a>""")

        return HttpResponseRedirect("./")
    else:
        _time_create_form = CreateNewTime()
    return render(request, 'time_manage/create.html', _var)

def list(request):
    _var = {"time_info" : TimeInfo.objects.all()}
    if request.method =="POST":
        if request.POST.get("filter_time_by_date"):
            _form = FilterTime(request.POST)
            if _form.is_valid():
                _time_date= _form.cleaned_data["_time_date"]
                _var["time_info"] = TimeInfo.objects.filter(time_date=_time_date)
                return render(request, 'time_manage/list.html', _var)
            else:
                print(f'\n\nform is not valid\n\n')
        else:
            print(f'\n\nresponse method is POST, {request.POST}\n\n')
    else:
        print(f'\n\nresponse method is not POST\n\n')
    return render(request, 'time_manage/list.html', _var)

def delete_time_confirm(request, _u_i):
    _var = {"time_info" : TimeInfo.objects.get(time_unique_id = _u_i)}
    return render(request, 'time_manage/deletetimeconfirm.html', _var)

def delete_time(request, _u_i):
    _time_info = TimeInfo.objects.get(time_unique_id = _u_i)
    _time_info.delete()
    return redirect(f'/time_manage/list/')

def save_player_list(_player_list, _music_info):
    #_player_list = ["instrument1 : player1", "instrument2 : player2", ..., "instrumentN : playerN"]
    for _p_i in _player_list:
        _player_info = [i.strip() for i in _p_i.split(sep=":")] #_player_info = [instrument_n, player_n]
        if len(_player_info) == 2:
            player_info = Player(player_name = _player_info[1], player_instrument = _player_info[0], music = _music_info)
            player_info.save()

def manage(request, _u_i):
    _time_info = TimeInfo.objects.get(time_unique_id = _u_i)
    _music_add_form = AddMusic()
    _player_list_form = AddPlayer()
    _var = {"time_info" : _time_info, "music_add_form" : _music_add_form, "player_list_form" : _player_list_form}

    if request.method == "POST":
        if request.POST.get("add_music"):
            _music_add_form = AddMusic(request.POST)
            _player_list_form = AddPlayer(request.POST)
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
                    save_player_list(_player_list, _music_info)
                    print('\nplayer list added\n')
                return redirect("./")
            print('\nform is not valid\n')
        elif request.POST.get("update_tv_breaktime"):
            _breaktime_form = UpdateBreaktime(request.POST)
            if _breaktime_form.is_valid():
                update_tv_breaktime(request, _breaktime_form.cleaned_data["_time_start"], _breaktime_form.cleaned_data["_time_end"])
            return redirect("./")
        elif request.POST.get("save_comment"):
            _time_comment_music = request.POST.get("comment_music")
            _time_comment_gigi = request.POST.get("comment_gigi")
            _time_comment_etc = request.POST.get("comment_etc")
            _time_info.time_comment_music = _time_comment_music
            _time_info.time_comment_gigi = _time_comment_gigi
            _time_info.time_comment_etc = _time_comment_etc
            _time_info.save()
            return redirect("./")
        else:
            print('\nresponse is not (add_music or update_tv_breaktime)\n')
            _music_add_form = AddMusic()
    return render(request, 'time_manage/manage.html', _var)

def delete_music_confirm(request, _u_i, _music_id):
    print("\n\ndelete_music_confirm clicked\n\n")
    _var = {"time_info" : TimeInfo.objects.get(time_unique_id = _u_i), "music_info" : Music.objects.get(id = _music_id)}
    return render(request, 'time_manage/deletemusicconfirm.html', _var)

def delete_music(request, _u_i, _music_id):
    print("\n\ndelete_music clicked\n\n")
    _music_info = Music.objects.get(id = _music_id)
    _music_info.delete()
    return redirect(f'/time_manage/{_u_i}/')

def insta_upload(request, _u_i):
    _var = {"time_info" : TimeInfo.objects.get(time_unique_id=_u_i)}
    return render(request, 'time_manage/instagramupload.html', _var)

def update_tv_music(request, _u_i, _music_id):
    tv_display_views.update_music(request, _u_i, _music_id)
    return redirect(f'/time_manage/{_u_i}/')

def update_tv_breaktime(request, _time_start, _time_end):
    tv_display_views.update_breaktime(request, _time_start, _time_end)
    return None

def edit_music(request, _u_i, _music_id):
    _time_info = TimeInfo.objects.get(time_unique_id=_u_i)
    _music_info = Music.objects.get(id=_music_id)
    _var = {"time_info" : _time_info, "music_info" : _music_info}

    if request.method == "POST":
        if request.POST.get("edit_music_request"):
            if request.POST.get("request") == "clicked":
                _music_info.music_request = True
            else:
                _music_info.music_request = False
            _music_info.save()

        elif request.POST.get("edit_music_source"):
            _music_source = request.POST.get("source")
            if len(_music_source) > 0:
                _music_info.music_source = _music_source
            _music_info.save()

        elif request.POST.get("edit_music_label_id"):
            _music_label_id = request.POST.get("label_id")
            if len(_music_label_id) > 0:
                _music_info.music_label_id = _music_label_id
            _music_info.save()

        elif request.POST.get("edit_music_composer"):
            _music_composer = request.POST.get("composer")
            if len(_music_composer) > 0:
                _music_info.music_composer = _music_composer
            _music_info.save()

        elif request.POST.get("edit_music_title"):
            _music_title = request.POST.get("title")
            if len(_music_title) > 0:
                _music_info.music_title = _music_title
            _music_info.save()

        elif request.POST.get("edit_music_orchestra"):
            _music_orchestra = request.POST.get("orchestra")
            if len(_music_orchestra) > 0:
                _music_info.music_orchestra = _music_orchestra
            _music_info.save()

        elif request.POST.get("edit_music_conductor"):
            _music_conductor = request.POST.get("conductor")
            if len(_music_conductor) > 0:
                _music_info.music_conductor = _music_conductor
            _music_info.save()

        elif request.POST.get("add_music_player"):
            print(f'\nadd_music_player clicked\n')
            player_info = Player(player_name = "새 연주자 이름", player_instrument = "새 연주자 악기", music = _music_info)
            player_info.save()

        else:
            print(f'\nPOST : {request.POST}\n')
            for _player_info in _music_info.player_set.all():
                if request.POST.get(f"edit_music_player_instrument{_player_info.id}"):
                    print(f'\nedit_music_player_instrument{_player_info.id} is clicked!\n')
                    _player_instrument = request.POST.get(f"instrument{_player_info.id}")
                    if len(_player_instrument) > 0:
                        _player_info.player_instrument = _player_instrument
                        _player_info.save()
                elif request.POST.get(f"edit_music_player_name{_player_info.id}"):
                    print(f'\nedit_music_player_name{_player_info.id} is clicked!\n')
                    _player_name = request.POST.get(f"namename{_player_info.id}")
                    if len(_player_name) > 0:
                        _player_info.player_name = _player_name
                        _player_info.save()
    else:
        print("\n\nrequest method is not POST\n\n")

    return render(request, 'time_manage/edit.html', _var)

def delete_player_confirm(request, _u_i, _music_id, _player_id):
    _var = {"time_info" : TimeInfo.objects.get(time_unique_id=_u_i), "music_info" : Music.objects.get(id=_music_id), "player_info" : Player.objects.get(id=_player_id)}
    return render(request, 'time_manage/deleteplayerconfirm.html', _var)

def delete_player(request, _u_i, _music_id, _player_id):
    _player_info = Player.objects.get(id = _player_id)
    _player_info.delete()
    return redirect(f'/time_manage/{_u_i}/edit_music/{_music_id}')