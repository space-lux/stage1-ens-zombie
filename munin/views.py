from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from munin.models import Agent,Ordre,TypeAgent
from django.contrib.sessions.models import Session

# Create your views here.

def home(request):
	agents=Agent.objects.all()
	return render(request,'munin/home.html',{'agents':agents})

def agents(request):
	request.session.clear_expired()
	return HttpResponse(serialize('json',Agent.objects.all()))

def ordres(request):
	return HttpResponse(serialize('json',Ordre.objects.all()))

def type_agents(request):
	return HttpResponse(serialize('json',TypeAgent.objects.all()))
