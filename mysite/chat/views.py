from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name, user_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'user_name': user_name
    })

def register(request):
    return render(request, 'chat/register.html')

def interaction(request):
    return render(request, 'chat/interaction.html')

    