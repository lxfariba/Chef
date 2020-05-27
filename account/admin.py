from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer


class CustomerAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
        ('Customer Info',
         {'fields': ('first_name', 'last_name', 'phone_number', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff')})
    )

    list_display = ('first_name', 'last_name', 'username', 'phone_number', 'address')
    search_fields = ('id', 'username', 'first_name', 'last_name')
    list_per_page = 100


admin.site.register(Customer, CustomerAdmin)