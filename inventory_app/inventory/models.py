from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from softdelete.models import *

# Create your models here.

class Manufacturer(SoftDeleteObject,models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)

    def get_absolute_url(self):
        return reverse("manufacturer-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Item(SoftDeleteObject,models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=100)
    nato_stock_number = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item-detail", kwargs={"pk": self.pk})

    @property
    def count_items(self):
        return Item_info.objects.count()


class PME(SoftDeleteObject,models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    items = models.ManyToManyField(Item)
    def get_absolute_url(self):
        return reverse("pme-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

class System(SoftDeleteObject,models.Model):
    name = models.CharField(max_length=50)
    desciption = models.TextField(null=True)
    pme = models.ManyToManyField(PME, default = 1)
    def get_absolute_url(self):
        return reverse("system-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

class Elimination(SoftDeleteObject,models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("elimination-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Inventory_location(SoftDeleteObject,models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)

    def get_absolute_url(self):
        return reverse("location-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Item_info(SoftDeleteObject,models.Model):
    commonName = models.CharField(max_length=50, null=True, blank = True)
    description = models.TextField(null=True)
    inventory_location = models.ForeignKey(Inventory_location, on_delete=models.CASCADE)
    elimination = models.ForeignKey(Elimination, on_delete=models.CASCADE)
    serialnumber = models.CharField(max_length=50)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=2)
    issued = models.BooleanField(null=True)

    def get_absolute_url(self):
        return reverse("info-detail", kwargs={"pk": self.pk})

    def __str__(self):
        if self.commonName:
            return f"{self.commonName} ({self.item.name})"
        else:
            return f"{self.item.name}"


    
