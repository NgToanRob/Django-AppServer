from django.db import models
from Account.models import Team, User

# Create your models here.
class FlightMode(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class AircraftType(models.Model):
    name = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.name


class Aircraft(models.Model):
    name = models.CharField(max_length=255, null=False)
    aircraft_type = models.ForeignKey(AircraftType, on_delete=models.CASCADE, \
                                        null=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False)
    status = models.BooleanField(null=False)
    activation_time =  models.DateTimeField(auto_now_add=True, null=False)
    serial_number = models.CharField(max_length=255, null=False)
    flight_controller_id = models.CharField(max_length=255, null=False)
    package = models.CharField(max_length=255, null=False)
    aircraft_lock =  models.BooleanField(null=False)

    def __str__(self):
        return self.name


class Realtime(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE ,\
                                null=False)
    flight_mode = models.ForeignKey(FlightMode, on_delete=models.CASCADE, \
                                    null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    task = models.DecimalField(max_digits=1000, decimal_places=5, null=False)
    spraying_rate = models.DecimalField(max_digits=1000, decimal_places=5, \
                                        null=False)
    route_spacing = models.DecimalField(max_digits=1000, decimal_places=5, \
                                        null=False)
    task_flight_speed = models.DecimalField(max_digits=1000, decimal_places=5, \
                                            null=False)
    height  = models.DecimalField(max_digits=1000, decimal_places=5, null=False)
    hopper_outlet_size = models.IntegerField(null=False)
    spinner_disk_speed = models.IntegerField(null=False)
    location = models.CharField(max_length=255, null=False)
    data = models.CharField(max_length=255, null=False)
    take_off_time = models.DateTimeField(null=False)
    landing_time = models.DateTimeField(null=False)
    flight_duration = models.DateTimeField(null=False)
    flight_record = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id) + ". " + self.user.__str__()