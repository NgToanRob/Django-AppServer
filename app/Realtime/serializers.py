from dataclasses import field, fields
from rest_framework.serializers import ModelSerializer
from .models import Aircraft, AircraftType, FlightMode, Realtime


class FlightModeSerializer(ModelSerializer):
    class Meta:
        model = FlightMode
        fields = '__all__'



class AircraftTypeSerializer(ModelSerializer):
    class Meta:
        model = AircraftType
        fields = '__all__'



class AircraftSerializer(ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'



class RealtimeSerializer(ModelSerializer):
    class Meta:
        model = Realtime
        # fields = [f.name for f in Realtime._meta.get_fields()]
        # fields = '__all__'
        exclude = ['user']