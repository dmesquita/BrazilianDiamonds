# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect

def addMarker(request, location):
	point = PointOfInterest(request.POST['name'], location)
	point.save()
	return HttpResponseRedirect(reverse('diamondslocation:result'))
	
def result(request):
	return HttpResponse("Funcionou!")
	
	
