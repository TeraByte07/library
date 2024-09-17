from django.contrib import admin
from .models import customUser, AdminUser  # Import your custom and proxy models

# Regular users admin
class RegularUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser')

    # Exclude staff and superusers
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_staff=False, is_superuser=False)

# Admin users admin
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser')

    # Only show staff and superusers
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_staff=True)

# Register both regular users and admin users separately
admin.site.register(customUser, RegularUserAdmin)  # For regular users
admin.site.register(AdminUser, AdminUserAdmin)  # For admin users (proxy model)
