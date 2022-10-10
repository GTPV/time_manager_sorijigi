from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),

    path('delete_time_confirm/<str:_u_i>/', views.delete_time_confirm, name='delete_time_confirm'),
    path('delete_time/<str:_u_i>/', views.delete_time, name='delete_time'),

    path('<str:_u_i>/', views.manage, name='manage'),

    path('<str:_u_i>/delete_music/<int:_music_id>/', views.delete_music, name='delete_music'),
    path('<str:_u_i>/delete_music_confirm/<int:_music_id>/', views.delete_music_confirm, name='delete_music_confirm'),

    path('<str:_u_i>/delete_player_confirm/<int:_music_id>/<int:_player_id>/', views.delete_player_confirm, name='delete_player_confirm'),
    path('<str:_u_i>/delete_player/<int:_music_id>/<int:_player_id>/', views.delete_player, name='delete_player'),

    path('<str:_u_i>/insta_upload/', views.insta_upload, name='insta_upload'),
    path('<str:_u_i>/update_tv_music/<int:_music_id>/', views.update_tv_music, name='upate_tv_music'),
    path('<str:_u_i>/edit_music/<int:_music_id>/', views.edit_music, name='edit_music'),
]