from django.shortcuts import render
from .models import AllDestinations
# Create your views here.
def all(request):
    dest = AllDestinations.objects.all()
    return render(request, 'destination.html', {'dests' : dest})
