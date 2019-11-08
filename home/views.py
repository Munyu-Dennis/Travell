from django.shortcuts import render
from .models import Destinations
# Create your views here.
def home(request):
    dest = Destinations.objects.all()
    return render(request, 'home.html', {'dests' : dest} )

