# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader

from diamondslocation.models import Marker, PointOfInterest
from diamondslocation.models import MarkerForm, PointOfInterestForm

def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request)
	results = PointOfInterest.objects.all()	
	return render_to_response('index.html', {"results": results,}, context_instance=context)
	
def form(request):
	marcador = PointOfInterest("doform",localization) 
	marcador.save()
	return HttpResponseRedirect(reverse('index.html'))
	
def addmarker(request):
	form = PointOfInterestForm(request.POST or None)
	if form.is_valid():
		fmodel = form.save()
		fmodel.save()
		return redirect(index)
		
	return render_to_response('addmarker.html',{'contact_form': form}, context_instance=RequestContext(request))
	

