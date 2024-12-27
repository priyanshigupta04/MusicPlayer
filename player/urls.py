from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
]

handler404 = player.views.handling_404Error
