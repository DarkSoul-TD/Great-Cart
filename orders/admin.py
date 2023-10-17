from django.contrib import admin
from .models import Order,OrderProduct,Payment


class OrderProductInlline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment','user','product','quantity','product_price','ordered')
    extra = 0



class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number','full_name', 'phone', 'email','city','order_total','tax','status','is_ordered']
    list_filter  = ['status','is_ordered']
    search_fields = ['order_number','first_name','last_name','phone','email']
    list_per_page = 20
    inlines = [OrderProductInlline]

# Register your models here.
admin.site.register(OrderProduct)
admin.site.register(Order,OrderAdmin)
admin.site.register(Payment)
