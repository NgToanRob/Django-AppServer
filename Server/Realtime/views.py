from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.utils.dateparse import parse_datetime
from .serializers import FlightModeSerializer, AircraftSerializer, AircraftTypeSerializer, RealtimeSerializer
from .models import Aircraft, FlightMode, Realtime, AircraftType
from rest_framework import viewsets, permissions

# Create your views here.
class FlightModeViewSet(viewsets.ModelViewSet):
    queryset = FlightMode.objects.all()
    serializer_class = FlightModeSerializer
    permission_classes = [permissions.IsAuthenticated]


class AircraftTypeViewSet(viewsets.ModelViewSet):
    queryset = AircraftType.objects.all()
    serializer_class = AircraftTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    permission_classes = [permissions.IsAuthenticated]

class RealtimeViewSet(viewsets.ModelViewSet):
    queryset = Realtime.objects.all()
    serializer_class = RealtimeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if request.data.get('id'):
            return super(RealtimeViewSet, self).update(request, *args, **kwargs)
        else:
            return super(RealtimeViewSet, self).create(request, *args, **kwargs)
        


class Adding(LoginRequiredMixin, View):
    def post(self, request):
        # References
        aircraft_id = request.POST.get('aircraft_id')
        flight_mode_id = request.POST.get('flight_mode_id')

        aircraft = Aircraft.objects.get(id=aircraft_id)
        flight_mode = FlightMode.objects.get(id=flight_mode_id)

        # Non-refer
        user = request.user
        task_area = request.POST.get('task_area')
        spraying_rate = request.POST.get('spraying_rate')
        route_spacing = request.POST.get('route_spacing')
        task_flight_speed = request.POST.get('task_flight_speed')
        height = request.POST.get('height')
        hopper_outlet_size = request.POST.get('hopper_outlet_size')
        spinner_disk_speed = request.POST.get('spinner_disk_speed')
        location = request.POST.get('location')
        data = request.POST.get('data')
        take_off_time = parse_datetime(request.POST.get('take_off_time'))
        landing_time = parse_datetime(request.POST.get('landing_time'))
        flight_duration = parse_datetime(request.POST.get('flight_duration'))
        flight_record = request.POST.get('flight_record')


        realtime_to_add = Realtime(
                                aircraft=aircraft,
                                user=user,
                                flight_mode=flight_mode,
                                task_area=task_area,
                                spraying_rate=spraying_rate,
                                route_spacing=route_spacing,
                                task_flight_speed=task_flight_speed,
                                height=height,
                                hopper_outlet_size=hopper_outlet_size,
                                spinner_disk_speed=spinner_disk_speed,
                                location=location,
                                data=data,
                                take_off_time=take_off_time,
                                landing_time=landing_time,
                                flight_duration=flight_duration,
                                flight_record=flight_record
                                )
        realtime_to_add.save()
        print("Successfully adding")
        # print(parse_datetime(flight_duration))
        # print(flight_duration)
        return HttpResponse("Successfully adding")

    def get(self, request):
        return render(request, 'Realtime/realtime.html')
        

