from django.contrib import admin

from .models import User, Rating, AvgRating


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'points']
    list_display_links = ['id', 'first_name', 'last_name', 'username']

    class Meta:
        model = User


class RatingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Rating._meta.fields]

    class Meta:
        model = Rating


class AvgRatingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AvgRating._meta.fields]

    class Meta:
        model = AvgRating


admin.site.register(User, MyUserAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(AvgRating, AvgRatingAdmin)
