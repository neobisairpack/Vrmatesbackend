from django.contrib import admin

from .models import User, Rating


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'email', 'points',
                    'avg_rating', 'rating_count', 'avg_rating_last_ten', 'canceled_posts_count', 'is_active']
    list_display_links = ['id', 'first_name', 'last_name', 'username']
    list_filter = ['is_active']
    search_fields = ['email', 'first_name', 'last_name']

    class Meta:
        model = User


class RatingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Rating._meta.fields]

    class Meta:
        model = Rating


admin.site.register(User, MyUserAdmin)
admin.site.register(Rating, RatingAdmin)
