from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime
from .scrap import GetActivities
import pytz
import re

ROOMS_NAMES = {
    704 : "704 - C++ room ",
    705 : "705 - Perl room",
    706 : "706 - Python room",
    708 : "708 - English room",
    709 : "709 - Swift room",
    710 : "710 - Shared room 2",
    711 : "711 - Haskell room",
    616 : "616 - Assembly room",
    615 : "615 - Hub room",
    610 : "610 - Lean room",
    609 : "609 - Typescript room",
    608 : "608 - Dart room",
    604 : "604 - Kotlin room",
    601 : "601 - C room"
}
FREE = "#9EFF7C"
OCCUPIED = "#E96B6B"

class Room:
    def __init__(self, name) -> None:
        self.name = name
        self.availability = {
            9 : True,
            10 : True,
            11 : True,
            12 : True,
            13 : True,
            14 : True,
            15 : True,
            16 : True,
            17 : True,
            18 : True
        }

def GetRoomAvailability():
    roomsPlanningData = GetActivities()

    roomsPlanning = dict()

    for room in ROOMS_NAMES:
        roomsPlanning[room] = Room(ROOMS_NAMES[room])

    for room in roomsPlanningData:
        extractedRoom = re.findall(r'(\d+)', room)
        if (len(extractedRoom) == 0):
            print(f"Error: room [{room}] has no number.")
            continue
        extractedRoom = int(extractedRoom[0])
        for activity in roomsPlanningData[room]:
            start = re.findall(r'(\d+):', activity[0])
            end = re.findall(r'(\d+):', activity[1])
            if (len(start) == 0 or len(end) == 0):
                print(f"Error: activity [{activity}] has no start or end.")
                continue
            start = int(start[0])
            end = int(end[0])
            for hour in range(start, end):
                roomsPlanning[extractedRoom].availability[hour] = False

    renderObject = dict()

    for room in roomsPlanning:
        renderObject["r" + str(room)] = roomsPlanning[room].name
        renderObject["r" + str(room) + "h"] = list()
        for hour in roomsPlanning[room].availability:
            if (roomsPlanning[room].availability[hour]):
                renderObject["r" + str(room) + "h"].append(FREE)
            else:
                renderObject["r" + str(room) + "h"].append(OCCUPIED)
    return renderObject

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def ExtractActivities(request):
    # request should be ajax and method should be GET.
    if is_ajax(request) and request.method == "GET":
        renderObject = GetRoomAvailability()
        return JsonResponse(renderObject, status = 200)
    return JsonResponse({}, status = 400)

# Create your views here.
def home_view(request):
    tz_pa = pytz.timezone('Europe/paris')
    now = datetime.now(tz_pa)
    current_time = now.strftime("%H:%M")

    renderObject = dict()
    renderObject = GetRoomAvailability()
    renderObject["current_time"] = current_time

    return render(request, 'main.html', renderObject)
