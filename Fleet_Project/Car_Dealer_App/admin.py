from django.contrib import admin
from .models import Area, CarDealer, Vehicles
# Register your models here.
class AreaAdmin(admin.ModelAdmin):
    Listdisplay=('pincode', 'city')

class CarDealerAdmin(admin.ModelAdmin):
    Listdisplay=('car_dealer', 'mobile')

class VehicleAdmin(admin.ModelAdmin):
    Listdisplay=('car_name', 'color')

admin.site.register(Area, AreaAdmin)
admin.site.register(CarDealer, CarDealerAdmin)
admin.site.register(Vehicles, VehicleAdmin)