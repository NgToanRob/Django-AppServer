from django.db import models
from Account.models import Team, User
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class FlightMode(models.Model):
    class Meta:
        pass

    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class AircraftType(models.Model):
    name = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.name


class Aircraft(models.Model):
    name = models.CharField(max_length=255, null=False)
    aircraft_type = models.ForeignKey(AircraftType, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, default=1)
    status = models.BooleanField(null=False)
    activation_time =  models.DateTimeField(null=False)
    serial_number = models.CharField(max_length=255, null=False)
    flight_controller_id = models.CharField(max_length=255, null=False)
    package = models.CharField(max_length=255, null=False)
    aircraft_lock =  models.BooleanField(null=False)

    def __str__(self):
        return self.name


class Realtime(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, null=True)
    flight_mode = models.ForeignKey(FlightMode, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    task_area = models.FloatField( null=True)
    location = models.CharField(max_length=255, null=False)

    spraying_rate = ArrayField(models.FloatField(), null=True)
    # array
    task_flight_speed = ArrayField(models.FloatField(), null=True)
    # array
    height  = ArrayField(models.FloatField(), null=True)
    # array
    hopper_outlet_size = ArrayField(models.FloatField(), null=True)
    # array
    spinner_disk_speed = ArrayField(models.FloatField(), null=True)
    # array
    data = ArrayField(ArrayField(models.FloatField()), null=True)
    # array [2] = {(x,y)}
    take_off_time = models.DateTimeField(null=False)
    landing_time = models.DateTimeField(null=False)
    
    # skip
    def __str__(self):
        return str(self.id)