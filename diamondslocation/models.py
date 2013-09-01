from django.db import models
from django.forms import ModelForm
from geoposition.fields import GeopositionField
from django import forms

# Create your models here.

class Marker(models.Model):	
	position = GeopositionField()	
	name = models.CharField(max_length=50,blank=False)
	email = models.EmailField(max_length=75,blank=False)	
	message = models.CharField(max_length=200,blank=True)
	link = models.CharField(max_length=200,blank=True)
	
	def __unicode__(self):
		return str(self.position)
			
	def __unicode__(self):
		return self.name
		
class MarkerForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'size':'40'}), label='Nome')
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': '(Nao sera publicado)','size':'40'}))
	message = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Quer dizer algo aos diamonds? (opcional)','size':'40'}), label='Mensagem')
	link = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Twitter, facebook, etc (opcional)','size':'40'}))
	class Meta:
		model = Marker		

