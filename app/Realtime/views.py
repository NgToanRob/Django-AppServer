from Server.settings import CACHE_TTL
from .serializers import FlightModeSerializer, AircraftSerializer, AircraftTypeSerializer, RealtimeSerializer
from .models import Aircraft, FlightMode, Realtime, AircraftType
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

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

    @method_decorator(cache_page(CACHE_TTL))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(CACHE_TTL))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


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
        response_data = {"id":serializer.data.get("id")}
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
        
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
        response_data = {"id":serializer.data.get("id")}
        return Response(response_data)

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
        if to_append["landing_time"] != None:
            old_data["landing_time"] = to_append["landing_time"] 

        to_append.pop("landing_time")
        for key in to_append:
            old_data[key].append(to_append[key][0])

        return old_data

        

