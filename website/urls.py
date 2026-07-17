from django.urls import path

from . import views

urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "send-enquiry/",
        views.send_enquiry,
        name="send_enquiry"
    ),


    path(
    "services/local-taxi-service/",
    views.local_taxi_service,
    name="local_taxi_service"
),

path(
    "services/bus-booking/",
    views.bus_booking,
    name="bus_booking"
),

path(
    "services/tempo-traveller/",
    views.tempo_traveller,
    name="tempo_traveller"
),

path(
    "services/outstation-tours/",
    views.outstation_tours,
    name="outstation_tours"
),

path(
    "services/pilgrimage-trips/",
    views.pilgrimage_trips,
    name="pilgrimage_trips"
),

path(
    "services/corporate-travel/",
    views.corporate_travel,
    name="corporate_travel"
),

]