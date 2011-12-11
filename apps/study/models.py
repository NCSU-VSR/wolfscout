from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.conf import settings
import datetime
import os


from apps.crawler.gpscollar.models import Collar,CollarData

# Create your models here.
# Add entry below, run commands: django-admin.py schemamigration apps.study --auto
#                                django-admin.py migrate apps.study
"""
class ShapeToAnalyze(models.Model):

These shapes are purely used to check for interactions, that's it

    #shape = models.

    def __unicode__(self):
        return str(self.pk)
"""
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

class AnimalInteractionGroup(models.Model):
    """
    Each Animal Interaction group will be linked to one study, and that is how we can avoid
    duplicate interactions throughout a study.
    """
    uploadPath = "interaction_files/"
    title = models.CharField(max_length=100,null=True,blank=True)
    study = models.ForeignKey(Study, related_name="AnimalInteractionStudyGroup")
    distance = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True)
    dbf_file = models.FileField(null=True,blank=True, upload_to=uploadPath)
    shp_file = models.FileField(null=True,blank=True, upload_to=uploadPath)
    shx_file = models.FileField(null=True,blank=True, upload_to=uploadPath)
    prj_file = models.FileField(null=True,blank=True, upload_to=uploadPath)
    zip_file = models.FileField(null=True,blank=True, upload_to=uploadPath)
    completed = models.BooleanField(default=False)
    def __unicode__(self):
        return str(self.pk)

class AnimalInteraction(models.Model):
    """
    Interactions will house interactions between an Animal and another Animal
    Each interaction will only be listed in the database once and should be automatically calculated as
    data is fed into the server.

    distance is in km
    """
    source_animal_data_point = models.ForeignKey(CollarData, related_name="AnimalSourceOfInteraction")
    destination_animal_data_point = models.ForeignKey(CollarData, related_name="AnimalDestinationOfInteraction")
    interaction_group = models.ForeignKey(AnimalInteractionGroup, related_name="AnimalInteractionGroupForInteraction", null=True, blank=True)
    distance = models.DecimalField(max_digits=15, decimal_places=5)

    def clean(self):
        """
        clean is used for validation purposes, if an interactione exists in the database already this will
        prevent it from being duplicated.
        """
        list_of_interactions = AnimalInteraction.objects.all()
        for interaction in list_of_interactions:
            if interaction.source_animal_data_point == self.source_animal_data_point:
                if interaction.destination_animal_data_point == self.destination_animal_data_point:
                    if interaction.interaction_group == self.interaction_group:
                        raise ValidationError("This item already exists")
            elif interaction.destination_animal_data_point == self.source_animal_data_point:
                if interaction.source_animal_data_point == self.destination_animal_data_point:
                    if interaction.interaction_group == self.interaction_group:
                        raise ValidationError("This item already exists")

    def __unicode__(self):
        return str(self.pk)

