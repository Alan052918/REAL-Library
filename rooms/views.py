from django.shortcuts import render

from .models import Room, RoomCustomer


def index(request):
    room_list = Room.objects.all()
    return render(request, "rooms/index.html", {"room_list": room_list})


def room_detail_view(request, pk):
    room = Room.objects.get(pk=pk)
    room_customers = RoomCustomer.objects.filter(room__id=room.id)
    return render(
        request,
        "rooms/room_detail.html",
        {"room": room, "room_customers": room_customers},
    )
