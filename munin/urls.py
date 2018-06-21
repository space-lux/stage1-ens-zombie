from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.home),
	url(r'^agents.json$',views.agents),
	url(r'^ordres.json$',views.ordres),
	url(r'^type_agents.json$',views.type_agents),
]
