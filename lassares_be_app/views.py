from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import fdr_18001_0_11_Serializer, testdata_Serializer
from .models import fdr_18001_0_11_Model, testdata_Model

# Create your views here.
class fdr_18001_0_11_View(viewsets.ReadOnlyModelViewSet):
    queryset = fdr_18001_0_11_Model.objects.all()
    serializer_class = fdr_18001_0_11_Serializer

class testdata_View(viewsets.ReadOnlyModelViewSet):
    queryset = testdata_Model.objects.all()
    serializer_class = testdata_Serializer

