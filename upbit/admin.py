from django.contrib import admin
from .models import UpbitDayCandle, UpbitMarket, UpbitMinuteCandle, UpbitMonthCandle, UpbitTicker, UpbitTicks, UpbitWeekCandle

# Register your models here.
admin.site.register(UpbitDayCandle)
admin.site.register(UpbitMarket)
admin.site.register(UpbitMinuteCandle)
admin.site.register(UpbitMonthCandle)
admin.site.register(UpbitTicker)
admin.site.register(UpbitTicks)
admin.site.register(UpbitWeekCandle)