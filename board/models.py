# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=20)
    year = models.DateField()
    registration = models.CharField(max_length=10)
    specification = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car'


class Profile(models.Model):
    time_received = models.DateTimeField()
    start_pos_lat = models.DecimalField(max_digits=8, decimal_places=5)
    start_pos_long = models.DecimalField(max_digits=8, decimal_places=5)
    end_pos_lat = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)
    end_pos_long = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)
    key = models.CharField(max_length=10)
    surveyor = models.ForeignKey('Surveyor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profile'


class Surveyor(models.Model):
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    key = models.CharField(max_length=10)
    car = models.ForeignKey(Car, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'surveyor'
