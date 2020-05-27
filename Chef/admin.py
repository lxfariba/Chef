from django.contrib import admin
from .models import Gallery, Contact


class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None, {'fields': ('first_name', 'last_name', 'email', 'message')}
        ),
    )

    list_display = ['email', 'message']


admin.site.register(Gallery)
admin.site.register(Contact, ContactAdmin)


# from django.contrib.auth.admin import UserAdmin
# from account.models import Customer
#
#
# class CustomerAdmin(UserAdmin):
#     fieldsets = (
#         (None, {'fields': ('username', 'password', 'email')}),
#         ('Customer Info',
#          {'fields': ('first_name', 'last_name', 'phone_number', 'address')}),
#         ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff')})
#     )
#
#     list_display = ('first_name', 'last_name', 'username', 'phone_number', 'address')
#     search_fields = ('id', 'username', 'first_name', 'last_name')
#     list_per_page = 100
#
#
# admin.site.register(Customer, CustomerAdmin)