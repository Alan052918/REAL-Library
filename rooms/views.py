from collections import defaultdict

from django.shortcuts import render

from .models import Room, RoomCustomer


def index(request):
    room_list = Room.objects.all()
    capacity_to_room = defaultdict(list)
    for room in room_list:
        capacity_to_room[room.capacity].append(room)
    room_list = capacity_to_room.values()
    print(room_list)

    return render(request, "rooms/index.html", {"room_list": room_list})


def room_detail_view(request, pk):
    room = Room.objects.get(pk=pk)
    room_customers = RoomCustomer.objects.filter(room__id=room.id)
    return render(
        request,
        "rooms/room_detail.html",
        {"room": room, "room_customers": room_customers},
    )
