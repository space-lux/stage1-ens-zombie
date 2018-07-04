from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.home),
	url(r'^jeu.html$',views.jeu),
	url(r'^suppr_ordre$',views.suppr_ordre),
	url(r'^ajout_ordre$',views.ajout_ordre),
	url(r'^maj_ordre$',views.maj_ordre),
	url(r'^maj_nom$',views.maj_nom),
	url(r'^data.json$',views.data),
	url(r'^joueurs.json$',views.joueurs),
	url(r'^type_agents.json$',views.type_agents),
]
