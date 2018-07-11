from django.db import models
from munin.mot import mot

# Create your models here.

class TypeAgent(models.Model):
	nom=models.TextField(null=True)
	puissance=models.CharField(max_length=50)
	prix=models.CharField(max_length=50)
	prix_achat=models.CharField(max_length=50)
	
	def __str__(self):
		return self.nom

class Joueur(models.Model):
	nom=models.CharField(max_length=50,null=True,default=mot)
	argent=models.CharField(max_length=50,default='0')
	session=models.ForeignKey('sessions.Session',null=True,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.nom

class Agent(models.Model):
	nom=models.TextField(null=True,default=mot)
	type_agent=models.ForeignKey('TypeAgent',null=True,on_delete=models.CASCADE)
	joueur=models.ForeignKey('Joueur',null=True,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.nom

class Ordre(models.Model):
	prix=models.CharField(max_length=50,default="0")
	puissance=models.CharField(max_length=50,default="0")
	agent=models.ForeignKey('Agent',null=True,on_delete=models.CASCADE)
