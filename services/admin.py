from django.contrib import admin

from .models import *


class ServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields]

    class Meta:
        model = Service


class ServiceImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ServiceImage._meta.fields]

    class Meta:
        model = ServiceImage


class RequestServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RequestService._meta.fields]

    class Meta:
        model = RequestService


class SupportAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Support._meta.fields]
    search_fields = ['name', 'date']

    class Meta:
        model = Support


class ProvideServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProvideService._meta.fields]

    class Meta:
        model = ProvideService


class RequestProvideServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RequestProvideService._meta.fields]

    class Meta:
        model = RequestProvideService


class ProvideServiceImagesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RequestProvideService._meta.fields]

    class Meta:
        model = ProvideServiceImage


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceImage, ServiceImageAdmin)
admin.site.register(RequestService, RequestServiceAdmin)
admin.site.register(Support, SupportAdmin)
admin.site.register(ProvideService, ProvideServiceAdmin)
admin.site.register(ProvideServiceImage, ProvideServiceImagesAdmin)
admin.site.register(RequestProvideService, RequestProvideServiceAdmin)
