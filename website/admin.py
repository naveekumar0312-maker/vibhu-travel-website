from django.contrib import admin

from .models import Enquiry


@admin.register(Enquiry)

class EnquiryAdmin(admin.ModelAdmin):

    list_display = (

        "id",

        "name",

        "phone",

        "vehicle",

        "pickup",

        "destination",

        "status",

        "created_at",

    )

    list_filter = (

        "vehicle",

        "status",

        "created_at",

    )

    search_fields = (

        "name",

        "phone",

        "pickup",

        "destination",

    )

    list_editable = (

        "status",

    )

    ordering = (

        "-created_at",

    )