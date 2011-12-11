#### Django Imports ####
from django.db import models
#### Local Imports #####
from apps.crawler.gpscollar.models import Collar, CollarData
# Create your models here.
class Species(models.Model):
    """
    Species act as their biological definition.
    A specimen may be long to them.
    Disease notes may be recorded, etc.
    """
    name = models.CharField(max_length=100, unique=True)
    notes = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return str(self.name)

class Animal(models.Model):
    """
    Animals that are being tracked in some fashion.
    Possibilities include a collar GPS unit, weather info, or custom sensors
    """

    AGE_CHOICES = (
        ('J', 'Juvenile'),
        ('SA', 'Subadult'),
        ('A', 'Adult'),
    )
    collar = models.ForeignKey(Collar, null=True, blank=True)
    common_name = models.CharField(max_length=50, unique=True)
    age = models.CharField(max_length=50, null=True, blank=True, choices=AGE_CHOICES)
    sex = models.CharField(max_length=50, null=True, blank=True)
    species = models.ForeignKey(Species, null=True, blank=True)

    def __unicode__(self):
        return str(self.common_name)

    def get_fields(self):
        # make a list of field/values.
        return [(field.name, field.value_to_string(self)) for field in Animal._meta.fields]
