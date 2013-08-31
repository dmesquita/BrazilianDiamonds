from django.db import models
from django.forms import ModelForm
from geoposition.fields import GeopositionField

# Create your models here.

class Marker(models.Model):	
	position = GeopositionField()	
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=200)
	message = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	
	def __unicode__(self):
		return str(self.position)
			
	def __unicode__(self):
		return self.name
		
class MarkerForm(ModelForm):
	class Meta:
		model = Marker		

