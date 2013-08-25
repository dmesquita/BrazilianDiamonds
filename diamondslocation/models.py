from django.db import models
from geoposition.fields import GeopositionField

# Create your models here.

class PointOfInterest(models.Model):
	name = models.CharField(max_length=100)
	position = GeopositionField()
	def __unicode__(self):
		return self.name

class Marker(models.Model):
	name = models.ForeignKey(PointOfInterest)
	message = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name
