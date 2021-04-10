from django.db import models

# Create your models here.
class PullRequest(models.Model):
    #Modelo de PR creados para visualizar despues
    author =  models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=50)

