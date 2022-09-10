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
    aircraft = models.ForeignKey(Aircraft, on_delete=models.SET_NULL, null=True)
    flight_mode = models.ForeignKey(FlightMode, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    task_area = models.DecimalField(max_digits=10, decimal_places=5, null=True)
    spraying_rate = ArrayField(models.DecimalField(max_digits=10, decimal_places=5))
    # array
    task_flight_speed = ArrayField(models.DecimalField(max_digits=10, decimal_places=5), null=True)
    # array
    height  = ArrayField(models.DecimalField(max_digits=10, decimal_places=5))
    # array
    hopper_outlet_size = ArrayField(models.DecimalField(max_digits=10, decimal_places=5))
    # array
    spinner_disk_speed = ArrayField(models.DecimalField(max_digits=10, decimal_places=5))
    # array
    location = models.CharField(max_length=255, null=False)
    data = ArrayField(ArrayField(models.DecimalField(max_digits=10, decimal_places=5)))
    # array [2] = {(x,y)}
    take_off_time = models.DateTimeField(null=False)
    landing_time = models.DateTimeField(null=False)
    # landing_time - take_off_time
    @property
    def duration(self):
        if self.take_off_time is not None and self.landing_time is not None:
            return self.landing_time - self.take_off_time

    flight_record = models.IntegerField(default=duration)
    # skip
    def __str__(self):
        return str(self.id)