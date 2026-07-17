from django.contrib import admin
from django.utils.html import format_html
from .models import Enquiry, Vehicle


# ==========================================
# ENQUIRY ADMIN
# ==========================================

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "phone",
        "vehicle",
        "pickup",
        "destination",
        "travel_date",
        "members",
        "status",
        "created_at",
    )

    list_filter = (
        "vehicle",
        "status",
        "travel_date",
        "created_at",
    )

    search_fields = (
        "name",
        "phone",
        "email",
        "pickup",
        "destination",
    )

    list_editable = (
        "status",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    date_hierarchy = "created_at"

    list_per_page = 20

    fieldsets = (

        ("Customer Details", {

            "fields": (
                "name",
                "phone",
                "email",
            )

        }),

        ("Trip Information", {

            "fields": (
                "vehicle",
                "pickup",
                "destination",
                "travel_date",
                "members",
                "trip_details",
            )

        }),

        ("Enquiry Status", {

            "fields": (
                "status",
            )

        }),

        ("System Information", {

            "classes": ("collapse",),

            "fields": (
                "created_at",
                "updated_at",
            )

        }),

    )


# ==========================================
# VEHICLE ADMIN
# ==========================================

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    list_display = (
        "image_preview",
        "name",
        "vehicle_type",
        "seats",
        "price",
        "available",
        "created_at",
    )

    list_filter = (
        "vehicle_type",
        "available",
    )

    search_fields = (
        "name",
        "vehicle_type",
    )

    list_editable = (
        "available",
    )

    ordering = (
        "vehicle_type",
    )

    readonly_fields = (
        "image_preview",
        "created_at",
    )

    list_per_page = 20

    fieldsets = (

        ("Vehicle Details", {

            "fields": (
                "name",
                "vehicle_type",
                "seats",
                "price",
                "description",
                "available",
            )

        }),

        ("Vehicle Image", {

            "fields": (
                "image",
                "image_preview",
            )

        }),

        ("System Information", {

            "classes": ("collapse",),

            "fields": (
                "created_at",
            )

        }),

    )

    def image_preview(self, obj):

        if obj.image:

            return format_html(
                '<img src="{}" width="120" height="70" style="border-radius:8px;object-fit:cover;" />',
                obj.image.url
            )

        return "No Image"

    image_preview.short_description = "Preview"
    
admin.site.site_header = "Vibhu Travel Hub Administration"

admin.site.site_title = "Vibhu Travel Hub Admin"

admin.site.index_title = "Welcome to Vibhu Travel Hub Dashboard"