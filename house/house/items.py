# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from zhenghe.models import SecondHouse
from zhenghe.models import NewHouse
from zhenghe.models import RentHouse

class HouseItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = SecondHouse
    pass
class NewHouseItem(DjangoItem):
    django_model=NewHouse
    pass
class RentHouseItem(DjangoItem):
    django_model=RentHouse
    pass