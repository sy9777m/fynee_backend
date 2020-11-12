from django.db import models


class KrxStockListig(models.Model):
    name = models.CharField(max_length=256)
    symbol = models.CharField(max_length=256)
    sector = models.CharField(max_length=256)
    industry = models.CharField(max_length=256)
    listing_day = models.DateField()
    settle_month = models.DateField()
    representative = models.CharField(max_length=256)
    homepage = models.CharField(max_length=2048)
    region = models.CharField(max_length=256)

    class Meta:
        db_table = 'krx_listing'

    def __str__(self) -> str: self.name


class NaverBusinessDay(models.Model):
    business_day = models.DateField()

    class Meta:
        db_table = 'business_day'

    def __str__(self) -> str: self.business_day
