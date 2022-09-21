from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.utils.dateparse import parse_datetime
from django.core import serializers
from .serializers import FlightModeSerializer, AircraftSerializer, AircraftTypeSerializer, RealtimeSerializer
from .models import Aircraft, FlightMode, Realtime, AircraftType
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

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

    # Override functions in CreateModelMixin
    def create(self, request, *args, **kwargs):
        """
        It creates a new instance of the model, and returns a serialized version of
        the new instance
        
        @param request The request object.
        @return The serializer.data is being returned.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, request)
        headers = self.get_success_headers(serializer.data)

        # Need to return id to update and lock status from aircraft
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
    def perform_create(self, serializer, request):
        serializer.save(user = request.user)


    # Override functions in UpdateModelMixin
    def update(self, request, *args, **kwargs):
        """
        It takes the data from the request, appends it to the data from the
        instance, and then passes it to the serializer
        
        @param request The request object.
        @return The serializer.data is being returned.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data  = self.append_data(instance, request.data)
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def append_data(self, instance, to_append):
        """
        It takes in a dictionary of data, and a dictionary of data to append. It then
        appends the data to append to the data, and returns the data
        
        @param instance the instance of the model that you want to update
        @param to_append {'altitude': [0.0], 'latitude': [0.0], 'longitude': [0.0],
        'pitch': [0.0], 'roll': [0.0], 'yaw': [0.0], 'velocity': [0
        @return The data is being returned in the form of a dictionary.
        """
        old_data = dict(RealtimeSerializer(instance).data)
        print(old_data)
        if to_append["landing_time"] != None:
            old_data["landing_time"] = to_append["landing_time"] 

        to_append.pop("landing_time")
        print(type(to_append))
        print(to_append)
        for key in to_append:
            print(old_data[key])
            old_data[key].append(to_append[key][0])
            # vanas ddeef laf neen guiwr raw data hay array

        return old_data


    



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
        

