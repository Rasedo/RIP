from django.db import models


class IceCream(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=30, blank=True, null=True)
    type_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'ice_creams'


class IceCreamShop(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    image = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ice_cream_shops'
