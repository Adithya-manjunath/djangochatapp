from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('room/<str:room_name>/<str:user_name>', views.room, name='room'),
]