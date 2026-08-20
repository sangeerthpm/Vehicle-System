from django.urls import path

from .views import (
    VehicleListCreateAPIView,
    VehicleDetailAPIView,
    BookingListCreateAPIView,
    BookingDetailAPIView,

)

urlpatterns = [

    # Vehicle APIs
    path('vehicles/',VehicleListCreateAPIView.as_view(),name='vehicle-list-create'),
    path('vehicles/<int:pk>/',VehicleDetailAPIView.as_view(),name='vehicle-detail'),

    # Booking APIs
    path('bookings/',BookingListCreateAPIView.as_view(),name='booking-list-create'),
    path('bookings/<int:pk>/',BookingDetailAPIView.as_view(),name='booking-detail'),
]