from django.contrib import admin

from .models import *


class DeliveryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Delivery._meta.fields]

    class Meta:
        model = Delivery

    def save_model(self, request, obj, form, change):
        obj.requester = request.user
        obj.save()


class DeliveryImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DeliveryImage._meta.fields]

    class Meta:
        model = DeliveryImage


class RequestDeliveryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RequestDelivery._meta.fields]

    class Meta:
        model = RequestDelivery

    def save_model(self, request, obj, form, change):
        obj.requester = request.user
        obj.save()


class PickUpAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PickUp._meta.fields]

    class Meta:
        model = PickUp

    def save_model(self, request, obj, form, change):
        obj.requester = request.user
        obj.save()


class RequestPickUpAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RequestPickUp._meta.fields]

    class Meta:
        model = RequestPickUp

    def save_model(self, request, obj, form, change):
        obj.requester = request.user
        obj.save()


class HostingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Hosting._meta.fields]

    class Meta:
        model = Hosting

    def save_model(self, request, obj, form, change):
        obj.requester = request.user
        obj.save()


class RequestHostingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RequestHosting._meta.fields]

    class Meta:
        model = RequestHosting

    def save_model(self, request, obj, form, change):
        obj.requester = request.user
        obj.save()


class SupportAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Support._meta.fields]
    search_fields = ['name', 'date']

    class Meta:
        model = Support


class ProvideDeliveryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProvideDelivery._meta.fields]

    class Meta:
        model = ProvideDelivery

    def save_model(self, request, obj, form, change):
        obj.provider = request.user
        obj.save()


class ProvidePickUpAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProvidePickUp._meta.fields]

    class Meta:
        model = ProvidePickUp

    def save_model(self, request, obj, form, change):
        obj.provider = request.user
        obj.save()


class ProvideHostingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProvideHosting._meta.fields]

    class Meta:
        model = ProvideHosting

    def save_model(self, request, obj, form, change):
        obj.provider = request.user
        obj.save()


admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(DeliveryImage, DeliveryImageAdmin)
admin.site.register(RequestDelivery, RequestDeliveryAdmin)
admin.site.register(PickUp, PickUpAdmin)
admin.site.register(RequestPickUp, RequestPickUpAdmin)
admin.site.register(Hosting, HostingAdmin)
admin.site.register(RequestHosting, RequestHostingAdmin)
admin.site.register(Support, SupportAdmin)
admin.site.register(ProvideDelivery, ProvideDeliveryAdmin)
admin.site.register(ProvidePickUp, ProvidePickUpAdmin)
admin.site.register(ProvideHosting, ProvideHostingAdmin)
