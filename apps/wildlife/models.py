#### Django Imports ####
from django.db import models
#### Local Imports #####
from apps.crawler.gpscollar.models import Collar, CollarData
# Create your models here.
class Species(models.Model):
    """
    Species act as their biological definition.
    A specimen may belong to them.
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
    age_class = models.CharField(max_length=50, null=True, blank=True, choices=AGE_CHOICES)
    sex = models.CharField(max_length=50, null=True, blank=True)
    species = models.ForeignKey(Species, null=True, blank=True)

    #Demographic fields

    date = models.CharField(max_length=50, null=True, blank=True) #Date model.DateTimeField(null=True, blank=True)
    time = models.CharField(max_length=50, null=True, blank=True) #Time model.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    trap = models.CharField(max_length=10, null=True, blank=True)
    crowntorump = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True)
    chest = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True)
    neck = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True)
    weight = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True)
    blood = models.BooleanField(default=False)
    hair = models.BooleanField(default=False)
    ticks = models.BooleanField(default=False)
    feces = models.BooleanField(default=False)
    status = models.CharField(max_length=50, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)


    def __unicode__(self):
        return str(self.common_name)

    def get_fields(self):
        # make a list of field/values.
        return [(field.name, field.value_to_string(self)) for field in Animal._meta.fields]
