from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('flightmode', views.FlightModeViewSet)
router.register('aircrafttype', views.AircraftTypeViewSet)
router.register('aircraft', views.AircraftViewSet)
router.register('realtime', views.RealtimeViewSet)

'''
/flightmode/ - GET - get all
/flightmode/ - POST - create
/flightmode/{id} - GET - get with id
/flightmode/{id} - PUT - update
/flightmode/{id} - DELETE - delete
'''

urlpatterns = [
    path('', include(router.urls))
]