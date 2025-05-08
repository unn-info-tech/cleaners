from django.contrib import admin
from .models import Service, RoomTag, FeatureTag, ExtraService, Order

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'individual_price')
    filter_horizontal = ('room_tags', 'feature_tags')  # Horizontal filter for many-to-many fields


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price', 'order_date')
    list_filter = ('order_date',)  # Filter orders by date
    search_fields = ('id',)  # Enable searching by order ID
    filter_horizontal = ('service', 'extra_service')  # Horizontal filter for many-to-many relationships

# Register models with the admin site
admin.site.register(Service, ServiceAdmin)
admin.site.register(RoomTag)
admin.site.register(FeatureTag)
admin.site.register(ExtraService)
admin.site.register(Order, OrderAdmin)  # Register Order model with custom admin
