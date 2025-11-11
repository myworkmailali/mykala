from django.contrib import admin

from .models import ShippingAddress,Order,OrderItems

admin.site.register(ShippingAddress)
#admin.site.register(Order)
admin.site.register(OrderItems)

class OrderItemInline(admin.TabularInline):
    model = OrderItems
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]