# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesbotItem(scrapy.Item):
    # define the fields for your item here like:
    highestCat = scrapy.Field()
    subCat = scrapy.Field()
    urlTag = scrapy.Field()
    websiteName = scrapy.Field()
    websiteUrl = scrapy.Field()
