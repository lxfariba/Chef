from django.contrib import admin
from .models import Food, FoodQuantity, Order


class FoodAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None, {'fields': ('category', 'name', 'price', 'description', 'picture_food')}
        ),
    )

    list_display = ['name', 'category', 'price', 'picture_food']


admin.site.register(Food, FoodAdmin)
admin.site.register(FoodQuantity)
admin.site.register(Order)