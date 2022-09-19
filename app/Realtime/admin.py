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
    list_display = ['aircraft', 'flight_mode', 'user', 'task_area', \
                    'spraying_rate', 'location', 'task_flight_speed', 'height' , \
                    'hopper_outlet_size', 'spinner_disk_speed', 'data', 'take_off_time', 'landing_time']
    ordering = ['id']

    
admin.site.register(Aircraft, AircraftAdmin)
admin.site.register(AircraftType, AircraftTypeAdmin)
admin.site.register(FlightMode, FlightModeAdmin)
admin.site.register(Realtime, RealtimeAdmin)

