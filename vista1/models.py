from django.db import models

from django.db import models
# Create your models here.
class Registro(models.Model):
    """ """
    email = models.EmailField()
    timestamp_in = models.DateTimeField(auto_now_add=True)
    temperatura = models.IntegerField(blank=True, null=True)
    oxigenacion = models.IntegerField(blank=True, null=True)
    def __unicode__(self):
        return self.email