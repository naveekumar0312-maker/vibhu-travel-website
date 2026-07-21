from urllib.parse import quote
from django.shortcuts import redirect, render
from .models import Enquiry
from django.http import HttpResponse


def home(request):
    return render(request, "website/home.html")


def send_enquiry(request):

    if request.method == "POST":

        travel_date = request.POST.get("travel_date")

        enquiry = Enquiry.objects.create(
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email", ""),
            vehicle=request.POST.get("vehicle"),
            pickup=request.POST.get("pickup"),
            destination=request.POST.get("destination"),
            travel_date=travel_date,
            members=int(request.POST.get("members", 1)),
            trip_details=request.POST.get("trip_details"),
        )

        message = f""" *Vibhu Travel Hub*

Name: {enquiry.name}
Phone: {enquiry.phone}
Vehicle: {enquiry.vehicle}
Pickup: {enquiry.pickup}
Destination: {enquiry.destination}
Travel Date: {enquiry.travel_date}
Members: {enquiry.members}

Trip Details:
{enquiry.trip_details}
"""

        whatsapp = f"https://wa.me/919655866660?text={quote(message)}"

        return redirect(whatsapp)

    return redirect("home")

def local_taxi_service(request):
    return render(request, "services/local_taxi_service.html")


def bus_booking(request):
    return render(request, "services/bus_booking.html")


def tempo_traveller(request):
    return render(request, "services/tempo_traveller.html")


def outstation_tours(request):
    return render(request, "services/outstation_tours.html")


def pilgrimage_trips(request):
    return render(request, "services/pilgrimage_trips.html")


def corporate_travel(request):
    return render(request, "services/corporate_travel.html")



def robots_txt(request):

    lines = [

        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/login/",
        "Disallow: /admin/logout/",
        "Sitemap: https://vibhutravelhub.com/sitemap.xml",

    ]

    return HttpResponse("\n".join(lines), content_type="text/plain")