from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.serializers import serialize
from munin.models import Agent,Ordre,TypeAgent,Joueur
from django.contrib.sessions.models import Session
import random

# Create your views here.
def assignerJoueur(request):
	if Joueur.objects.filter(session=request.session.session_key).count():
		request.session['joueur']=Joueur.objects.get(session=request.session.session_key)
	else:
		request.session['joueur']=Joueur.objects.create(session=Session.objects.get(session_key=request.session.session_key))
		request.session['joueur'].save()
		aall=Agent.objects.all()
		if sum([float(a.type_agent.puissance) for a in aall])<0: # équilibrage à peu près du réseau
			tall=TypeAgent.objects.filter(puissance__gte=0)
		else:
			tall=TypeAgent.objects.filter(puissance__lt=0)
		t=random.choice(tall)
		a=Agent.objects.create(nom=t.nom+' de '+request.session['joueur'].nom,type_agent=t,joueur=request.session['joueur'])
		Ordre.objects.create(agent=a,prix=0,puissance=0)

def home(request):
	request.session.clear_expired()
	request.session['session créée']=True # trick dégueu pour que l'objet Session soit créé pour la prochaine requête
	r=render(request,'munin/home.html')
	r['Cache-Control']='no-cache,no-store'
	return r

def data(request):
	request.session['session créée']=True
	if Joueur.objects.filter(session=request.session.session_key).count():
		r=HttpResponse(serialize('json',list(Agent.objects.all())+list(Ordre.objects.all())+list([Joueur.objects.get(session=request.session.session_key)]),fields=('prix','puissance','nom','agent','joueur')))
	else:
		r=HttpResponse(serialize('json',list(Agent.objects.all())+list(Ordre.objects.all()),fields=('prix','puissance','nom','agent','joueur')))
	r['Cache-Control']='no-cache,no-store'
	return r

def joueurs(request):
	r=HttpResponse(serialize('json',Joueur.objects.all(),fields=('nom')))
	r['Cache-Control']='no-cache,no-store'
	return r

def type_agents(request):
	request.session.clear_expired()
	assignerJoueur(request)
	r=HttpResponse(serialize('json',TypeAgent.objects.all()))
	r['Cache-Control']='no-cache,no-store'
	return r
	
def jeu(request):
	request.session.clear_expired()
	if not(Joueur.objects.filter(session=request.session.session_key).count()):
		return redirect('/')
	assignerJoueur(request)
	if request.method == 'POST':
		if 'nom' in request.POST.keys():
			if 'pk' in request.POST.keys():
				if request.session['joueur'].agent_set.filter(pk=request.POST['pk']).count():
					agent=request.session['joueur'].agent_set.get(pk=request.POST['pk'])
					agent.nom=request.POST['nom']
					agent.save()
			else:
				request.session['joueur'].nom=request.POST['nom']
				request.session['joueur'].save()
	r=render(request,'munin/jeu.html',{'joueur':request.session['joueur']})
	r['Cache-Control']='no-cache,no-store'
	return r

def suppr_ordre(request):
	r=HttpResponse("POST!!!")
	if request.method == 'POST':
		r=HttpResponse("Paramètres !")
		if 'pk' in request.POST.keys():
			if Ordre.objects.filter(pk=request.POST['pk']).count():
				if Ordre.objects.get(pk=request.POST['pk']).agent in request.session['joueur'].agent_set.all():
					Ordre.objects.get(pk=request.POST['pk']).delete()
					r=HttpResponse("yay")
	r['Cache-Control']='no-cache,no-store'
	return r

def maj_ordre(request):
	r=HttpResponse("POST!!!")
	if request.method == 'POST':
		r=HttpResponse("Paramètres !")
		if 'pk' in request.POST.keys():
			if Ordre.objects.filter(pk=request.POST['pk']).count():
				if Ordre.objects.get(pk=request.POST['pk']).agent in request.session['joueur'].agent_set.all():
					o=Ordre.objects.get(pk=request.POST['pk'])
					if 'puissance' in request.POST.keys():
						o.puissance=request.POST['puissance']
					if 'prix' in request.POST.keys():
						o.prix=request.POST['prix']
					o.save()
					r=HttpResponse("yay")
	r['Cache-Control']='no-cache,no-store'
	return r
	
def ajout_ordre(request):
	r=HttpResponse("POST!!!",status=403)
	if request.method == 'POST':
		if 'agent' in request.POST.keys():
			if request.session['joueur'].agent_set.filter(pk=request.POST['agent']).count():
				o=Ordre.objects.create(agent=Agent.objects.get(pk=request.POST['agent']))
				if 'puissance' in request.POST.keys():
					o.puissance=request.POST['puissance']
				if 'prix' in request.POST.keys():
					o.prix=request.POST['prix']
				o.save()
				r=HttpResponse(o.pk)
	return r
	
