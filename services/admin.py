from django.contrib import admin

from .models import Service, Hosting


class ServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields]

    class Meta:
        model = Service


class HostingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Hosting._meta.fields]

    class Meta:
        model = Hosting


admin.site.register(Service, ServiceAdmin)
admin.site.register(Hosting, HostingAdmin)
