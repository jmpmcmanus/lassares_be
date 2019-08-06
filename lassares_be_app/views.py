from django.shortcuts import render
from rest_framework import viewsets
from .serializers import fdr_18001_0_11_Serializer, testdata_Serializer
from .models import fdr_18001_0_11_Model, testdata_Model
from .filters import TestdataFilter

# Create your views here.
class fdr_18001_0_11_View(viewsets.ReadOnlyModelViewSet):
    queryset = fdr_18001_0_11_Model.objects.all()
    serializer_class = fdr_18001_0_11_Serializer

class testdata_View(viewsets.ModelViewSet):
    queryset = testdata_Model.objects.all()
    serializer_class = testdata_Serializer
    filter_class = TestdataFilter

