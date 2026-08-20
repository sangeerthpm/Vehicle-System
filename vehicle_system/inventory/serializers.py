from django.utils import timezone
from rest_framework import serializers
from .models import Vehicle, Booking


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['total_amount']

    def validate_customer_phone(self, value):

        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain only digits."
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must be exactly 10 digits."
            )

        return value

    def validate_start_date(self, value):

        if value < timezone.localdate():
            raise serializers.ValidationError(
                "Start date cannot be in the past."
            )

        return value

    def validate(self, data):

        start_date = data.get('start_date')
        end_date = data.get('end_date')
        vehicle = data.get('vehicle')

        # End date validation
        if start_date and end_date:

            if end_date <= start_date:
                raise serializers.ValidationError({
                    'end_date': 'End date must be after start date.'
                })

        # Vehicle availability
        if vehicle and not vehicle.is_available:
            raise serializers.ValidationError({
                'vehicle': 'This vehicle is currently unavailable.'
            })

        # Double booking check
        if vehicle and start_date and end_date:

            existing_booking = Booking.objects.filter(
                vehicle=vehicle,
                start_date__lt=end_date,
                end_date__gt=start_date
            ).exists()

            if existing_booking:
                raise serializers.ValidationError({
                    'vehicle': 'This vehicle is already booked for these dates.'
                })

        return data