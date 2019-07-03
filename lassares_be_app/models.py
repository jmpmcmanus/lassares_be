from django.contrib.gis.db import models
#from django.db import models

# Create your models here.
class fdr_18001_0_11_Model(models.Model):
    ogc_fid = models.IntegerField(primary_key=True)
    wkb_geometry = models.MultiLineStringField()
    powerline = models.TextField(50,null=False)
