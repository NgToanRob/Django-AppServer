from django.contrib import admin
from .models import Aircraft, AircraftType, Data, FlightMode, Realtime

# Register your models here.
admin.site.register(Aircraft)
admin.site.register(AircraftType)
admin.site.register(FlightMode)
admin.site.register(Data)
admin.site.register(Realtime)

