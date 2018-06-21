from django.db import models

# Create your models here.

class TypeAgent(models.Model):
	nom=models.TextField(null=True)
	puissance=models.CharField(max_length=50)
	prix=models.CharField(max_length=50)
	
	def __str__(self):
		return self.nom

class Agent(models.Model):
	nom=models.TextField(null=True)
	type_agent=models.ForeignKey('TypeAgent',null=True)
	session=models.ForeignKey('sessions.Session',null=True)
	
	def __str__(self):
		return self.nom

class Ordre(models.Model):
	prix=models.CharField(max_length=50)
	puissance=models.CharField(max_length=50)
	agent=models.ForeignKey('Agent',null=True)
