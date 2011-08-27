from django.db import models

# Create your models here.
class species(models.Model):
    """
    Species act as their biological definition.
    A specimen may be long to them.
    Disease notes may be recorded, etc.
    """
    name = models.CharField(max_length=100, unique=True)
    notes = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return str(self.name)

class specimen(models.Model):
    """
    Specimen are animals that are being tracked in some fashion.
    Possibilities include a collar GPS unit, weather info, or custom sensors
    """

    collar_ID = models.CharField(max_length=50, null=True, blank=True, unique=True)
    common_name = models.CharField(max_length=50, null=True, blank=True)
    species = models.ForeignKey(species, null=True, blank=True)

    def __unicode__(self):
        return str(self.common_name)

class collar_data(models.Model):
    """
    Collar Data should relate to a single specimen at a given time
    it has a ton of fields that map it to a given specimen
    Field names were given by their similarity to the output format
    """

    GMT_DATETIME = models.DateTimeField()
    LMT_DATETIME = models.DateTimeField()

    ECEF_X = models.IntegerField(null=True, blank=True)
    ECEF_Y = models.IntegerField(null=True, blank=True)
    ECEF_Z = models.IntegerField(null=True, blank=True)
    LATITUDE = models.DecimalField(max_digits=12, null=True, blank=True)
    LONGITUDE = models.DecimalField(max_digits=12, null=True, blank=True)
    HEIGHT = models.DecimalField(max_digits=12, null=True, blank=True)
    DOP = models.DecimalField(max_digits=5, null=True, blank=True)
    NAV = (('3D', '3D'),('U', 'Unknown'))
    VALIDATED = models.BooleanField(default=False)
    SATS_USED = models.IntegerField(null=True, blank=True)
    CH1_SATID = models.IntegerField(null=True, blank=True)
    CH1_CN = models.IntegerField(null=True, blank=True)
    CH2_SATID = models.IntegerField(null=True, blank=True)
    CH2_CN = models.IntegerField(null=True, blank=True)
    CH3_SATID = models.IntegerField(null=True, blank=True)
    CH3_CN = models.IntegerField(null=True, blank=True)
    CH4_SATID = models.IntegerField(null=True, blank=True)
    CH4_CN = models.IntegerField(null=True, blank=True)
    CH5_SATID = models.IntegerField(null=True, blank=True)
    CH5_CN = models.IntegerField(null=True, blank=True)
    CH6_SATID = models.IntegerField(null=True, blank=True)
    CH6_CN = models.IntegerField(null=True, blank=True)
    CH7_SATID = models.IntegerField(null=True, blank=True)
    CH7_CN = models.IntegerField(null=True, blank=True)
    CH8_SATID = models.IntegerField(null=True, blank=True)
    CH8_CN = models.IntegerField(null=True, blank=True)
    CH9_SATID = models.IntegerField(null=True, blank=True)
    CH9_CN = models.IntegerField(null=True, blank=True)
    CH10_SATID = models.IntegerField(null=True, blank=True)
    CH10_CN = models.IntegerField(null=True, blank=True)
    CH11_SATID = models.IntegerField(null=True, blank=True)
    CH11_CN = models.IntegerField(null=True, blank=True)
    CH12_SATID = models.IntegerField(null=True, blank=True)
    CH12_CN = models.IntegerField(null=True, blank=True)
    MAIN_VOL = models.DecimalField(max_digits=5, null=True, blank=True)
    BU_VOL = models.DecimalField(max_digits=5, null=True, blank=True)
    TEMP = models.IntegerField(null=True, blank=True)
    REMARKS =models.TextField(null=True, blank=True)

    def __unicode__(self):
        return str(self.id)