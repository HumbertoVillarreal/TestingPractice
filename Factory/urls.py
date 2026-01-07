from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r"factories", FactoryViewSet, basename="factory")
router.register(r"lines", LineViewSet, basename="line")
router.register(r"machines", MachineViewSet, basename="machine")

urlpatterns = router.urls
 