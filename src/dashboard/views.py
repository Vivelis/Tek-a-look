from django.shortcuts import render

# Create your views here.
def home_view(request):
    r704 = "704 - c++ room "
    r705 = "705 - perl room"
    r706 = "706 - python room"
    r708 = "708 - english room"
    r709 = "709 swift room"
    r710 = "710 - shared room 2"
    r711 = "711 - haskell room"
    r616 = "616 - assembly room"
    r615 = "615 - hub room"
    r610 = "610 - lean room"
    r609 = "609 - typescript room"
    r608 = "608 - dart room"
    r604 = "604 - kotlin room"
    r601 = "601 - c room"

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
        'r601': r601 
        })
