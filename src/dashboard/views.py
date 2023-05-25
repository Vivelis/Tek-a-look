from django.shortcuts import render

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
