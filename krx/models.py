from django.db import models


# Create your models here.
class KRXListing(models.Model):
    symbol = models.CharField(max_length=16)
    market = models.CharField(max_length=16)
    name = models.CharField(max_length=64)
    sector = models.CharField(max_length=128)
    industry = models.CharField(max_length=128)
    listingDate = models.DateField()
    settleMonth = models.CharField(max_length=8)
    representative = models.CharField(max_length=64)
    homepage = models.CharField(max_length=512)
    region = models.CharField(max_length=16)
    data_source = models.CharField(max_length=32)

    class Meta:
        db_table = 'KRX Listing'

    def __str__(self) -> str:
        return self.name


class KRXDelisting(models.Model):
    symbol = models.CharField(max_length=16)
    name = models.CharField(max_length=64)
    delisting_date = models.DateField()
    reason = models.CharField(max_length=512)

    class Meta:
        db_table = 'KRX Delisting Data'
        verbose_name = 'KRX Delisting'

    def __str__(self) -> str:
        return self.name