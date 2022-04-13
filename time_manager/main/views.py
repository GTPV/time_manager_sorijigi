from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>this is main page(time_manager/main/views.py)</h1><br></br><a href='/time_manage/'>Time manage</a><br></br><a href='/admin'>Admin</a>")