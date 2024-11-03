from django.contrib import admin
from .models import AboutModel, ServiceModel, ContactModel, StaffModel, TestimonialModel


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    search_fields = ['id', 'text', 'is_selected', 'created_at', 'selected_at']
    list_display = ['id', 'short_text', 'is_selected', 'created_at', 'selected_at']

    def short_text(self, obj):
        return obj.text[:50]

@admin.register(ServiceModel)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description', 'is_available', 'updated_at']

    def short_description(self, obj):
        return obj.description[:75]

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_answered', 'service__name', 'short_message', 'created_at']
    list_filter = ['name', 'email','phone_number', 'is_answered']
    search_fields = ['name', 'email','phone_number']

    def short_message(self, obj):
        return obj.message[:50]


@admin.register(StaffModel)
class StaffModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'web_display']
    search_fields = ['name', 'position']
    list_filter = ['name', 'position','web_display']


@admin.register(TestimonialModel)
class TestimonialModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_displayed', 'created_at']
    search_fields = ['name', 'is_displayed', 'created_at']
    list_filter = ['name', 'is_displayed', 'created_at']


