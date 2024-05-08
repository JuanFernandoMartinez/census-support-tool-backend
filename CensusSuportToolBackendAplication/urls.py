from rest_framework import routers
from .api import ComunityViewSet

routers = routers.DefaultRouter()   
routers.register('api/comunity', ComunityViewSet, 'comunity')
urlpatterns = routers.urls
