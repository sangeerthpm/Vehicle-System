from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Vehicle, Booking
from .serializers import VehicleSerializer, BookingSerializer
from django.shortcuts import render

class VehicleListCreateAPIView(APIView):

    def get(self, request):

        vehicles = Vehicle.objects.all()

        # Brand filter
        brand = request.query_params.get('brand')

        if brand:
            vehicles = vehicles.filter(
                brand__iexact=brand
            )

        # Fuel type filter
        fuel_type = request.query_params.get('fuel_type')

        if fuel_type:
            vehicles = vehicles.filter(
                fuel_type__iexact=fuel_type
            )

        # Availability filter
        is_available = request.query_params.get('is_available')

        if is_available:

            if is_available.lower() == 'true':
                vehicles = vehicles.filter(
                    is_available=True
                )

            elif is_available.lower() == 'false':
                vehicles = vehicles.filter(
                    is_available=False
                )

        serializer = VehicleSerializer(
            vehicles,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = VehicleSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class VehicleDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return Vehicle.objects.get(pk=pk)

        except Vehicle.DoesNotExist:
            return None

    def get(self, request, pk):

        vehicle = self.get_object(pk)

        if vehicle is None:
            return Response(
                {'error': 'Vehicle not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = VehicleSerializer(vehicle)

        return Response(serializer.data)

    def put(self, request, pk):

        vehicle = self.get_object(pk)

        if vehicle is None:
            return Response(
                {'error': 'Vehicle not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = VehicleSerializer(
            vehicle,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):

        vehicle = self.get_object(pk)

        if vehicle is None:
            return Response(
                {'error': 'Vehicle not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        vehicle.delete()

        return Response(
            {'message': 'Vehicle deleted successfully.'},
            status=status.HTTP_204_NO_CONTENT
        )


class BookingListCreateAPIView(APIView):

    def get(self, request):

        bookings = Booking.objects.all()

        serializer = BookingSerializer(
            bookings,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = BookingSerializer(
            data=request.data
        )

        if serializer.is_valid():

            booking = serializer.save()

            return Response(
                BookingSerializer(booking).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class BookingDetailAPIView(APIView):

    def get(self, request, pk):

        try:
            booking = Booking.objects.get(pk=pk)

        except Booking.DoesNotExist:

            return Response(
                {'error': 'Booking not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BookingSerializer(booking)

        return Response(serializer.data)




def home(request):
    return render(request, 'vehicles/home.html')


def vehicle_detail_page(request, vehicle_id):
    return render(
        request,
        'vehicles/vehicle_detail.html',
        {
            'vehicle_id': vehicle_id
        }
    )


def booking_page(request, vehicle_id):
    return render(request,'vehicles/booking.html',{'vehicle_id': vehicle_id})