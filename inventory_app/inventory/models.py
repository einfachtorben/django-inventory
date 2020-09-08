from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    deleted_at = models.DateTimeField(null=True)

    def get_absolute_url(self):
        return reverse("manufacturer-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    deleted_at = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=100)
    nato_stock_number = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item-detail", kwargs={"pk": self.pk})


class PME(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    deleted_at = models.DateTimeField(null=True)
    items = models.ManyToManyField(Item)

    def get_absolute_url(self):
        return reverse("pme-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Elimination(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    deleted_at = models.DateTimeField(null=True)

    def get_absolute_url(self):
        return reverse("elimination-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Inventory_location(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    deleted_at = models.DateTimeField(null=True)

    def get_absolute_url(self):
        return reverse("location-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Item_info(models.Model):
    description = models.TextField(null=True)
    deleted_at = models.DateTimeField(null=True)
    inventory_location = models.ForeignKey(Inventory_location, on_delete=models.CASCADE)
    elimination = models.ForeignKey(Elimination, on_delete=models.CASCADE)
    serialnumber = models.CharField(max_length=50)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=2)

    def get_absolute_url(self):
        return reverse("info-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
