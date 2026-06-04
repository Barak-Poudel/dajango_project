from django.shortcuts import render, get_object_or_404
from .models import Room

def home(request):
    rooms = Room.objects.all()

    location = request.GET.get('location')
    max_rent = request.GET.get('max_rent')

    if location:
        rooms = rooms.filter(location__icontains=location)

    if max_rent:
        rooms = rooms.filter(rent__lte=max_rent)

    context = {
        'rooms': rooms
    }

    return render(request, 'rooms/home.html', context)


def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)

    return render(
        request,
        'rooms/room_detail.html',
        {'room': room}
    )