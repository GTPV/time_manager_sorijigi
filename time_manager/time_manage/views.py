from django.core.exceptions import *
from django.http import HttpResponseRedirect
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def index(response):
    return redirect('/time_manage/list')

def create(response):
    if response.method == "POST":
        _form = CreateNewTime(response.POST)

        if _form.is_valid():
            _manager = _form.cleaned_data["_time_manager"]
            _date = _form.cleaned_data["_time_date"]
            _start = _form.cleaned_data["_time_start"]
            _end = _form.cleaned_data["_time_end"]
            print(f'_manager : {_manager}, _date : {_date}, _start : {_start}, _end : {_end}')

            _time = TimeInfo(time_manager=_manager, time_date = _date, time_start = _start, time_end = _end)
            _time.save()
            return redirect("../")
        else:
            print(f'form is not valid')

        return HttpResponseRedirect("./")
    else:
        _form = CreateNewTime()
    return render(response, 'time_manage/create.html', {})

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
    _var = {"time_info" : _time_info}
    _var["i"] = 0

    if response.method == "POST":
        if response.POST.get("add_music"):
            _form = AddMusic(response.POST)
            if _form.is_valid():
                print('\n\nform_is_valid\n\n')
                _music_request = _form.cleaned_data['_music_request']
                _music_source = _form.cleaned_data['_music_source']
                _music_label_id = _form.cleaned_data['_music_label_id']
                _music_composer = _form.cleaned_data['_music_composer']
                _music_title = _form.cleaned_data['_music_title']
                _music_orchestra = _form.cleaned_data['_music_orchestra']
                _music_conductor = _form.cleaned_data['_music_conductor']

                if _music_label_id == "":
                    _music_label_id = '해당 없음'
                if _music_orchestra == "":
                    _music_orchestra = '해당 없음'
                if _music_conductor == "":
                    _music_conductor = '해당 없음'

                _time_info.music_set.create(music_request=_music_request, music_source=_music_source, music_label_id=_music_label_id, music_composer=_music_composer, music_title=_music_title, music_orchestra=_music_orchestra, music_conductor=_music_conductor)
                return redirect("./")
            print('\nform is not valid\n')
        else:
            print('\nresponse is not add_music\n')
            _form = AddMusic(response.POST)
    return render(response, 'time_manage/manage.html', _var)