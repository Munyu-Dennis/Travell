from django.shortcuts import render
from .models import Destinations
# Create your views here.
def home(request):
    dest = Destinations.objects.all()
    rnge = [1,2,3]
    return render(request, 'home.html', {'dests' : dest, 'range':rnge} )

