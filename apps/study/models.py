from django.db import models
from django.contrib.auth.models import User

import datetime

from apps.crawler.gpscollar.models import Collar
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
    members = models.ManyToManyField(User,related_name="membersForStudy",
                                         null=True,blank=True)
    title = models.CharField(max_length=100,null=False,blank=False)
    description = models.TextField(null=True, blank=True)
    last_accessed = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now())
    def __unicode__(self):
        return str(self.owner.username)