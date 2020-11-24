from django.db import models


# Create your models here.
class UpbitMarket(models.Model):
    market = models.CharField(max_length=16)
    korean_name = models.CharField(max_length=64)
    english_name = models.CharField(max_length=64)

    class Meta:
        db_table = 'Upbit Market'

    def __str__(self) -> str:
        return self.english_name


class UpbitTicker(models.Model):
    market = models.CharField(max_length=16)
    trade_date = models.CharField(max_length=8)
    trade_time = models.CharField(max_length=16)
    trade_date_kst = models.CharField(max_length=8)
    trade_time_kst = models.CharField(max_length=16)
    trade_timestamp = models.CharField(max_length=32)
    opening_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    trade_price = models.FloatField()
    prev_closing_price = models.FloatField()
    change = models.CharField(max_length=8)
    change_price = models.FloatField()
    change_rate = models.FloatField()
    signed_change_price = models.FloatField()
    signed_change_rate = models.FloatField()
    trade_volume = models.FloatField()
    acc_trade_price = models.FloatField()
    acc_trade_price_24h = models.FloatField()
    acc_trade_volume = models.FloatField()
    acc_trade_volume_24h = models.FloatField()
    highest_52_week_price = models.FloatField()
    highest_52_week_date = models.DateField()
    lowest_52_week_price = models.FloatField()
    lowest_52_week_date = models.DateField()
    timestamp = models.CharField(max_length=64)

    class Meta:
        db_table = 'Upbit Ticker'

    def __str__(self) -> str:
        return self.market


class UpbitMinuteCandle(models.Model):
    market = models.CharField(max_length=16)
    candle_date_time_utc = models.DateTimeField()
    candle_date_time_kst = models.DateTimeField()
    opening_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    trade_price = models.FloatField()
    timestamp = models.CharField(max_length=64)
    candle_acc_trade_price = models.FloatField()
    candle_acc_trade_volume = models.FloatField()
    unit = models.IntegerField()

    class Meta:
        db_table = 'Upbit Minute Candle'

    def __str__(self) -> str:
        return self.market


class UpbitDayCandle(models.Model):
    market = models.CharField(max_length=16)
    candle_date_time_utc = models.DateTimeField()
    candle_date_time_kst = models.DateTimeField()
    opening_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    trade_price = models.FloatField()
    timestamp = models.CharField(max_length=64)
    candle_acc_trade_price = models.FloatField()
    candle_acc_trade_volume = models.FloatField()
    prev_closing_price = models.FloatField()
    change_price = models.FloatField()
    change_rate = models.FloatField()

    class Meta:
        db_table = 'Upbit Day Candle'

    def __str__(self) -> str:
        return self.market


class UpbitWeekCandle(models.Model):
    market = models.CharField(max_length=16)
    candle_date_time_utc = models.DateTimeField()
    candle_date_time_kst = models.DateTimeField()
    opening_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    trade_price = models.FloatField()
    timestamp = models.CharField(max_length=64)
    candle_acc_trade_price = models.FloatField()
    candle_acc_trade_volume = models.FloatField()
    first_day_of_period = models.DateField()

    class Meta:
        db_table = 'Upbit Week Candle'

    def __str__(self) -> str:
        return self.market


class UpbitMonthCandle(models.Model):
    market = models.CharField(max_length=16)
    candle_date_time_utc = models.DateTimeField()
    candle_date_time_kst = models.DateTimeField()
    opening_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    trade_price = models.FloatField()
    timestamp = models.CharField(max_length=64)
    candle_acc_trade_price = models.FloatField()
    candle_acc_trade_volume = models.FloatField()
    first_day_of_period = models.DateField()

    class Meta:
        db_table = 'Upbit Month Candle'

    def __str__(self) -> str:
        return self.market


class UpbitTicks(models.Model):
    market = models.CharField(max_length=16)
    trade_date_utc = models.DateField()
    trade_time_utc = models.TimeField()
    timestamp = models.CharField(max_length=32)
    trade_price = models.FloatField()
    trade_volume = models.FloatField()
    prev_closing_price = models.FloatField()
    change_price = models.FloatField()
    ask_bid = models.CharField(max_length=8)
    sequential_id = models.CharField(max_length=64)

    class Meta:
        db_table = 'Upbit Tick Data'

    def __str__(self) -> str:
        return self.market