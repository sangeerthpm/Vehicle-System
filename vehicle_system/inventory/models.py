from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from decimal import Decimal


class Vehicle(models.Model):

    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    fuel_type = models.CharField(
        max_length=20,
        choices=FUEL_CHOICES
    )

    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.name}"


class Booking(models.Model):

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=10)

    start_date = models.DateField()
    end_date = models.DateField()

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def clean(self):

        # Phone validation
        if not self.customer_phone.isdigit():
            raise ValidationError(
                "Phone number must contain only digits."
            )

        if len(self.customer_phone) != 10:
            raise ValidationError(
                "Phone number must be exactly 10 digits."
            )

        # Start date validation
        today = timezone.localdate()

        if self.start_date < today:
            raise ValidationError(
                "Start date cannot be in the past."
            )

        # End date validation
        if self.end_date <= self.start_date:
            raise ValidationError(
                "End date must be after start date."
            )

        # Check overlapping bookings
        overlapping_booking = Booking.objects.filter(
            vehicle=self.vehicle,
            start_date__lt=self.end_date,
            end_date__gt=self.start_date
        ).exclude(pk=self.pk).exists()

        if overlapping_booking:
            raise ValidationError(
                "This vehicle is already booked for these dates."
            )

    def save(self, *args, **kwargs):

        self.full_clean()

        days = (self.end_date - self.start_date).days

        self.total_amount = (
            Decimal(days) * self.vehicle.price_per_day
        )

        super().save(*args, **kwargs)

        # Vehicle becomes unavailable
        self.vehicle.is_available = False
        self.vehicle.save()

    def __str__(self):
        return f"{self.customer_name} - {self.vehicle}"