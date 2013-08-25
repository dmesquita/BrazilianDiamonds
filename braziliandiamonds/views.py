# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader

from diamondslocation.models import Marker, PointOfInterest

def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request)
	results = PointOfInterest.objects.all()	
	return render_to_response('index.html', {"results": results,}, context_instance=context)
