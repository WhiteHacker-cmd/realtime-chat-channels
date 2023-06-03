from django.urls import path
from . import views



urlpatterns = [
    path('room/<slug:label>', views.chat_room, name='chat_room')
]