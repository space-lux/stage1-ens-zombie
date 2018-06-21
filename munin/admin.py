from django.contrib import admin
from munin.models import Agent, TypeAgent, Ordre
from django.contrib.sessions.models import Session

class TypeAgentAdmin(admin.ModelAdmin):
	list_display	= ('nom','puissance','prix')
	ordering		= ('puissance','prix','nom')
	search_fields	= ('nom',)

admin.site.register(TypeAgent,TypeAgentAdmin)
admin.site.register(Agent)
admin.site.register(Ordre)
admin.site.register(Session)

# Register your models here.
