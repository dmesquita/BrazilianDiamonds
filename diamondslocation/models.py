from django.db import models
from django.forms import ModelForm
from geoposition.fields import GeopositionField
from django import forms

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
		
class MarkerForm(forms.ModelForm):
	link = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Twitter, facebook, etc','size':'40'}))
	class Meta:
		model = Marker		

