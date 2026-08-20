from django.urls import path

from .views import (
    home,
    vehicle_detail_page,
    booking_page,
)


urlpatterns = [


    path('',home,name='home'),

    path('vehicle/<int:vehicle_id>/',vehicle_detail_page,name='vehicle-detail-page'),

    path('vehicle/<int:vehicle_id>/book/',booking_page,name='booking-page'),

]