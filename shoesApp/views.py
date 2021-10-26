from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from .models import Shoes


def index( request ):

    shoes = Shoes.objects.all()
    return render(request, 'index.html', {'shoes': shoes})



def contactus( request ):
    return render(request, 'contact.html')

def racingboots(request):
    return render (request, 'racing boots.html')

def collection( request ):
    return render(request, 'collection.html')

def shoes( request ):
    return render(request, 'shoes.html')




