from django.contrib import admin
from .models import AllDestinations
# Register your models here.
class ShowAll(admin.ModelAdmin):
    list_display = ('name', 'price', 'offer')

admin.site.register(AllDestinations, ShowAll)