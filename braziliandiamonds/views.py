# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext, loader

def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request)
	return HttpResponse(template.render(context))
