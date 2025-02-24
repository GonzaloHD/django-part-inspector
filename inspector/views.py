from django.shortcuts import render
from rest_framework import viewsets
from .models import Part, Inspection, Feature
from .serializers import PartSerializer, InspectionSerializer, FeatureSerializer

# Create your views here.

class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

class InspectionViewSet(viewsets.ModelViewSet):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
