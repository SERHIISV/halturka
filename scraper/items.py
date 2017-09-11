# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    URL = scrapy.Field()
    Price = scrapy.Field()
    Stock = scrapy.Field()
    Name = scrapy.Field()
    Brand = scrapy.Field()
    EAN = scrapy.Field()
    MPN = scrapy.Field()
    Description = scrapy.Field()
    Category = scrapy.Field()
    Shop_ID = scrapy.Field()
    Image = scrapy.Field()
    Promotext = scrapy.Field()
    Item = scrapy.Field()
    PriceInc = scrapy.Field()
    PriceExc = scrapy.Field()
    Id = scrapy.Field()
    ProductId = scrapy.Field()
