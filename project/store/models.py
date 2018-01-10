from django.db import models

class Thing(models.Model):
	description = models.CharField(max_length=20, primary_key=True)

class Another(models.Model):
	stuff = models.ManyToManyField(Thing)
