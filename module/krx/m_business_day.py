from bs4 import BeautifulSoup as bs
import requests as rq

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django
django.setup()

from backend.module.models import NaverBusinessDay


def naver_finance_business_day():
    url = 'https://finance.naver.com/sise/sise_index.nhn?code=KOSPI'

    res = rq.get(url)
    parse = bs(res.content)

    result = parse.find('span', {'id': 'time'}).text[0:10]
    result = result[0:4] + result[5:7] + result[8:10]

    return result
