from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartViewSet, InspectionViewSet, FeatureViewSet

# Create a router and register your viewsets with it
router = DefaultRouter()
router.register(r'parts', PartViewSet)
router.register(r'inspections', InspectionViewSet)
router.register(r'features', FeatureViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
]
