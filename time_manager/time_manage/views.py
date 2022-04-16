from django.core.exceptions import *
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .forms import *
from .models import *

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
    _var = {"time_info" : _time_info, "music_add_form" : _music_add_form}

    if response.method == "POST":
        if response.POST.get("add_music"):
            _music_add_form = AddMusic(response.POST)
            if _music_add_form.is_valid():
                print('\n\nform_is_valid\n\n')
                _time_info.music_set.create(**_music_add_form.cleaned_data)
                return redirect("./")
            print('\nform is not valid\n')
        else:
            print('\nresponse is not add_music\n')
            _music_add_form = AddMusic()
    return render(response, 'time_manage/manage.html', _var)

def delete_music(response, _u_i, _music_id):
    _music_info = Music.objects.get(id = _music_id)
    _music_info.delete()
    return redirect(f'/time_manage/{_u_i}/')