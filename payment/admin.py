from django.contrib import admin

from .models import ShippingAddress,Order,OrderItems

admin.site.register(ShippingAddress)
#admin.site.register(Order)
admin.site.register(OrderItems)

class OrderItemInline(admin.TabularInline):
    model = OrderItems
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    #fields = ['user','full_name','date_ordered']
    readonly_fields=('date_ordered','last_update')
    inlines = [OrderItemInline]