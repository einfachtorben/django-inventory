from django.contrib import admin
from inventory.models import (
    Elimination,
    PME,
    Inventory_location,
    Item,
    Item_info,
    Manufacturer,
)

# Register your models here.
admin.site.register(Elimination)
admin.site.register(PME)
admin.site.register(Inventory_location)
admin.site.register(Item)
admin.site.register(Item_info)
admin.site.register(Manufacturer)

