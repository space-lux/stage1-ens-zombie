from django.contrib import admin
from munin.models import Agent, TypeAgent, Ordre, Joueur
from django.contrib.sessions.models import Session

class TypeAgentAdmin(admin.ModelAdmin):
	list_display	= ('nom','puissance','prix')
	ordering		= ('puissance','prix','nom')
	search_fields	= ('nom',)
	
class OrdreAdmin(admin.ModelAdmin):
	list_display	= ('agent','puissance','prix')
	ordering		= ('puissance','prix','agent')

admin.site.register(TypeAgent,TypeAgentAdmin)
admin.site.register(Agent)
admin.site.register(Ordre,OrdreAdmin)
admin.site.register(Joueur)
admin.site.register(Session)

# Register your models here.
