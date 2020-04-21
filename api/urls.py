from django.urls import path,include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('movies',MovieViewSet)
router.register('rating',RatingViewSet)

urlpatterns = [
    path('',include(router.urls)),
]