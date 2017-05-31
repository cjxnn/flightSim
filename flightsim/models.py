from django.db import models

class Plane(models.Model):
	name = models.CharField(max_length=20)
	type = models.CharField(max_length=1)
	
class Flight(models.Model):
	flight_no = models.CharField(max_length=10)
	arrival_time = models.DateTimeField('time_arrived', null=True, blank=True)
	departure_time = models.DateTimeField('time_departed')
	plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
	gate_no = models.IntegerField(null=True, blank=True)