#Filtres persos
from django import template

register=template.Library()

register.filter('abs',lambda x:abs(x))
register.filter('float',lambda x:float(x))

@register.filter
def sort_by(objs,field):
	return objs.order_by(field)

