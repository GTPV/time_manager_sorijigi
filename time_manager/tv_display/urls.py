from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    #path('<str:_u_id>/', views.display_music, name='display_music'),
]