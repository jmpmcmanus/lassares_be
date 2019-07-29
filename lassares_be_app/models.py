from django.contrib.gis.db import models
#from django.db import models

# Create your models here.
class fdr_18001_0_11_Model(models.Model):
    ogc_fid = models.IntegerField(primary_key=True)
    wkb_geometry = models.MultiLineStringField(null=False)
    title = models.TextField(20,null=False)
    powerline = models.TextField(50,null=False)
    voltage = models.IntegerField(null=False)
    MONTH_DAY_YEAR = '%m/%d/%Y'
    MONTH_YEAR = '%m/%Y'
    DATE_CHOICE= (
                  (MONTH_DAY_YEAR, 'Month Day Year'),
                  (MONTH_YEAR, 'Month Year')
                 )
    service_date = models.CharField('Date Choice', choices=DATE_CHOICE,  max_length=10, null=False)

class testdata_Model(models.Model):
    ogc_fid = models.IntegerField(primary_key=True)
    wkb_geometry = models.PointField(null=False)
    device_id = models.TextField(10,null=False)
    timestamp = models.DateTimeField(null=False)
    job_id = models.TextField(10,null=False)
    concentrat = models.IntegerField(null=False)
    chem_id = models.TextField(10,null=False)
    amb_temp = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    rel_humid = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    precip = models.IntegerField(null=False)
    air_pressu = models.IntegerField(null=False)
    wind_speed = models.IntegerField(null=False)
    wind_direc = models.IntegerField(null=False)
