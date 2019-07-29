import rest_framework_filters as filters
from .models import testdata_Model

class TestdataFilter(filters.FilterSet):
   class Meta:
        model = testdata_Model
        fields = {
            'device_id': ['exact'],
            'job_id': ['exact'],
            'timestamp': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'concentrat':  ['exact', 'lt', 'gt', 'lte', 'gte'],
            'chem_id': ['exact'], 
            'amb_temp': ['exact', 'lt', 'gt', 'lte', 'gte'], 
            'rel_humid': ['exact', 'lt', 'gt', 'lte', 'gte'], 
            'precip': ['exact', 'lt', 'gt', 'lte', 'gte'], 
            'air_pressu': ['exact', 'lt', 'gt', 'lte', 'gte'], 
            'wind_speed': ['exact', 'lt', 'gt', 'lte', 'gte'], 
            'wind_direc': ['exact', 'lt', 'gt', 'lte', 'gte']
        }