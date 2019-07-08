#from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import fdr_18001_0_11_Model, testdata_Model

class fdr_18001_0_11_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = fdr_18001_0_11_Model
        geo_field = 'wkb_geometry'
        id_field='ogc_fid'
        fields= ('ogc_fid', 'powerline')

class testdata_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = testdata_Model
        geo_field = 'wkb_geometry'
        id_field='ogc_fid'
        fields= ('ogc_fid', 'measurement', 'value')

