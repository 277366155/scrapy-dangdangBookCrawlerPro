# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    title= scrapy.Field()
    url=scrapy.Field()
    price= scrapy.Field()
    realPrice= scrapy.Field()
    detail=scrapy.Field()
    author=scrapy.Field()
    press=scrapy.Field()

