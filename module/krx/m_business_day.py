from bs4 import BeautifulSoup as bs
import requests as rq

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django
django.setup()

from ..module.models import NaverBusinessDay


def naver_finance_business_day():
    url = 'https://finance.naver.com/sise/sise_index.nhn?code=KOSPI'

    res = rq.get(url)
    parse = bs(res.content)

    result = parse.find('span', {'id': 'time'}).text[0:10]
    result = result[0:4] + result[5:7] + result[8:10]

    return result


if __name__ == '__main__':
    business_day = naver_finance_business_day()
    NaverBusinessDay(business_day=business_day).save()
