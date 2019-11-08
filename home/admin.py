from django.contrib import admin
from .models import Destinations
# Register your models here.
class ShowDest(admin.ModelAdmin):
    list_display = ('name', 'price', 'offer')

admin.site.register(Destinations, ShowDest)


