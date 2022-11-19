from django.contrib import admin

# Register your models here.
from .models import Customer, Orders

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    Listdisplay=('user', 'mobile')

class OrdersAdmin(admin.ModelAdmin):
    Listdisplay=('user', 'vehicle')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Orders, OrdersAdmin)