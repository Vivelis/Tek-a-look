from django.shortcuts import render
from datetime import datetime
import pytz

# Create your views here.
def home_view(request):
    r704 = "704 - C++ room "
    r705 = "705 - Perl room"
    r706 = "706 - Python room"
    r708 = "708 - English room"
    r709 = "709 - Swift room"
    r710 = "710 - Shared room 2"
    r711 = "711 - Haskell room"
    r616 = "616 - Assembly room"
    r615 = "615 - Hub room"
    r610 = "610 - Lean room"
    r609 = "609 - Typescript room"
    r608 = "608 - Dart room"
    r604 = "604 - Kotlin room"
    r601 = "601 - C room"


    tz_pa = pytz.timezone('Europe/paris') 
    now = datetime.now(tz_pa)
    current_time = now.strftime("%H:%M")

    free = "#9EFF7C"
    occupied = "#E96B6B"

    r704h = [free, free, free, free, free, free, free, free, free, free]
    r705h = [free, free, free, free, free, free, free, free, free, free]
    r706h = [free, free, free, free, free, free, free, free, free, free]
    r708h = [free, free, free, free, free, free, free, free, free, free]
    r709h = [free, free, free, free, free, free, free, free, free, free]
    r710h = [free, free, free, free, free, free, free, free, free, free]
    r711h = [free, free, free, free, free, free, free, free, free, free]
    r616h = [free, free, free, free, free, free, free, free, free, free]
    r615h = [free, free, free, free, free, free, free, free, free, free]
    r610h = [free, free, free, free, free, free, free, free, free, free]
    r609h = [free, free, free, free, free, free, free, free, free, free]
    r608h = [free, free, free, free, free, free, free, free, free, free]
    r604h = [free, free, free, free, free, free, free, free, free, free]
    r601h = [free, free, free, free, free, free, free, free, free, free]

    return render(request, 'main.html', {
        'r704': r704, 
        'r705': r705, 
        'r706': r706,
        'r708': r708, 
        'r709': r709, 
        'r710': r710, 
        'r711': r711, 
        'r616': r616, 
        'r615': r615, 
        'r610': r610, 
        'r609': r609, 
        'r608': r608, 
        'r604': r604, 
        'r601': r601,
        'current_time': current_time,
        'r704h': r704h,
        'r705h': r705h,
        'r706h': r706h,
        'r708h': r708h,
        'r709h': r709h,
        'r710h': r710h,
        'r711h': r711h,
        'r616h': r616h,
        'r615h': r615h,
        'r610h': r610h,
        'r609h': r609h,
        'r608h': r608h,
        'r604h': r604h,
        'r601h': r601h,
        })
