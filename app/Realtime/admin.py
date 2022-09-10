from django.contrib import admin
from .models import Aircraft, AircraftType, FlightMode, Realtime


# Register your models here.
class FlightModeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    ordering = ['id']


class AircraftTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    ordering = ['id']


class AircraftAdmin(admin.ModelAdmin):
    list_display = ['id', 'aircraft_type', 'status', 'activation_time',\
                    'serial_number', 'flight_controller_id', 'package', 'aircraft_lock' ]
    search_fields = ['name']
    list_filter = ['name', 'aircraft_type', 'status', 'aircraft_lock']
    ordering = ['id']


class RealtimeAdmin(admin.ModelAdmin):
    list_display = [field.name.__str__() for field in Realtime._meta.get_fields()]
    search_fields = ['aircraft', 'flight_mode', 'user', 'task', 'location']
    ordering = ['id']

    
admin.site.register(Aircraft, AircraftAdmin)
admin.site.register(AircraftType, AircraftTypeAdmin)
admin.site.register(FlightMode, FlightModeAdmin)
admin.site.register(Realtime, RealtimeAdmin)

