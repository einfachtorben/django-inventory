from django.contrib import admin
from inventory.models import (
    Elimination,
    PME,
    Inventory_location,
    Item,
    Item_info,
    Manufacturer,
    System
)
from softdelete.admin import *
from django.contrib.admin import ModelAdmin

# Register your models here.
#admin.site.register(Elimination, SoftDeleteObjectAdmin)
#admin.site.register(PME, SoftDeleteObjectAdmin)
#admin.site.register(Inventory_location, SoftDeleteObjectAdmin)
#admin.site.register(Item, SoftDeleteObjectAdmin)
#admin.site.register(Item_info, SoftDeleteObjectAdmin)
#admin.site.register(Manufacturer, SoftDeleteObjectAdmin)
#admin.site.register(System,SoftDeleteObjectAdmin)

@admin.register(Item)
class ItemAdmin(SoftDeleteObjectAdmin):
    list_display = ('id', '__str__', 'count_items')
    readonly_fields = ['deleted']

@admin.register(Item_info)
class ItemInfoAdmin(SoftDeleteObjectAdmin):
    list_display = ('id', '__str__', 'inventory_location')
    readonly_fields = ['deleted']

@admin.register(Elimination, PME, Inventory_location, Manufacturer,System)
class CustomAdminDisplay(SoftDeleteObjectAdmin):
    list_display = ('id', '__str__')
    readonly_fields = ['deleted']


