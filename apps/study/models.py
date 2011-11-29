from django.db import models
from django.contrib.auth.models import User

import datetime

from apps.crawler.gpscollar.models import Collar,CollarData
# Create your models here.
# Add entry below, run commands: django-admin.py schemamigration apps.study --auto
#                                django-admin.py migrate apps.study

class Study(models.Model):
    """
    Study sets up the owner for an study,
    All of the collars used, and the other members.
    """
    owner = models.ForeignKey(User)

    collars = models.ManyToManyField(Collar,related_name="collarsForStudy",
                                     null=True,blank=True)
    collars.help_text = ''
    members = models.ManyToManyField(User,related_name="membersForStudy",
                                         null=True,blank=True)
    members.help_text = ''
    title = models.CharField(max_length=100,null=False,blank=False)
    description = models.TextField(null=True, blank=True)
    last_accessed = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now())
    def __unicode__(self):
        return str(self.pk)

class AnimalInteraction(models.Model):
    """
    Interactions will house interactions between an Animal and another Animal
    Each interaction will only be listed in the database once and should be automatically calculated as
    data is fed into the server.

    distance is in km
    """
    source_animal = models.ForeignKey(CollarData, related_name="AnimalSourceOfInteraction")
    destination_animal = models.ForeignKey(CollarData, related_name="AnimalDestinationOfInteraction")
    distance = models.DecimalField(max_digits=15, decimal_places=5)

    def __unicode__(self):
        return str(self.pk)