from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),
    path('<str:_u_i>/', views.manage, name='manage'),
    path('<str:_u_i>/delete/<int:_music_id>/', views.delete_music, name='delete_music'),
    path('<str:_u_i>/insta_upload/', views.insta_upload, name='insta_upload'),
]