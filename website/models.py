from django.db import models


class Enquiry(models.Model):

    VEHICLE_CHOICES = [

        ("Taxi", "Taxi"),
        ("SUV", "SUV"),
        ("Tempo Traveller", "Tempo Traveller"),
        ("Mini Bus", "Mini Bus"),
        ("Bus", "Bus"),

    ]

    STATUS_CHOICES = [

        ("New", "New"),
        ("Contacted", "Contacted"),
        ("Confirmed", "Confirmed"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),

    ]

    # Customer Details
    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    email = models.EmailField(blank=True, null=True)

    # Trip Details
    vehicle = models.CharField(
        max_length=50,
        choices=VEHICLE_CHOICES
    )

    pickup = models.CharField(max_length=255)

    destination = models.CharField(max_length=255)

    travel_date = models.DateField()

    members = models.PositiveIntegerField(default=1)

    trip_details = models.TextField()

    # Enquiry Status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="New"
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["-created_at"]

        verbose_name = "Travel Enquiry"

        verbose_name_plural = "Travel Enquiries"

    def __str__(self):

        return f"{self.name} | {self.vehicle} | {self.destination}"

class Vehicle(models.Model):
    VEHICLE_CHOICES = [
        ("Sedan", "Sedan"),
        ("Ertiga", "Ertiga"),
        ("Innova Crysta", "Innova Crysta"),
        ("Tempo Traveller AC", "Tempo Traveller AC"),
        ("Tempo Traveller Non AC", "Tempo Traveller Non AC"),
        ("Traveller Coach 20", "Traveller Coach 20"),
        ("Traveller Coach 26", "Traveller Coach 26"),
        ("Mini Bus", "Mini Bus"),
        ("Coach Bus", "Coach Bus"),
        ("Luxury Bus", "Luxury Bus"),
    ]

    name = models.CharField(max_length=100)

    vehicle_type = models.CharField(
        max_length=100,
        choices=VEHICLE_CHOICES
    )

    seats = models.PositiveIntegerField()

    image = models.ImageField(upload_to="vehicles/")

    price = models.CharField(max_length=50)

    description = models.TextField()

    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name