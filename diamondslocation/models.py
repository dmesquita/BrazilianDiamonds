from django.db import models
from django.forms import ModelForm
from geoposition.fields import GeopositionField

# Create your models here.

class PointOfInterest(models.Model):
	name = models.CharField(max_length=100)
	position = GeopositionField()
	def __unicode__(self):
		return str(self.position)
		
	def getName(self):
		return self.name

class Marker(models.Model):
	name = models.ForeignKey(PointOfInterest)
	email = models.CharField(max_length=200)
	message = models.CharField(max_length=200)
	link = models.CharField(max_length=200)	
	def __unicode__(self):
		return self.name
		
class MarkerForm(ModelForm):
	class Meta:
		model = Marker
		exclude = ('name',)
		
class PointOfInterestForm(ModelForm):
	class Meta:
		model = PointOfInterest
