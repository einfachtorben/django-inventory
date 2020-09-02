# Generated by Django 3.0.8 on 2020-08-03 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Elimination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('deleted_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventory_location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('deleted_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('deleted_at', models.DateTimeField()),
                ('barcode', models.CharField(max_length=100)),
                ('nato_stock_number', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('deleted_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PME',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('deleted_at', models.DateTimeField()),
                ('items', models.ManyToManyField(to='inventory.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Item_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('deleted_at', models.DateTimeField()),
                ('serialnumber', models.CharField(max_length=50)),
                ('elimination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Elimination')),
                ('inventory_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Inventory_location')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Manufacturer'),
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]