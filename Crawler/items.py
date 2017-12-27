# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy as sc


class CrawlerItem(sc.Item):
    # define the fields for your item here like:
    #name = scrapy.Field()
    name = sc.Field()
    urlkey = sc.Field()
    urlcr = sc.Field()
    urladdr = sc.Field()


class myXmlItem(sc.Item):
    # define the fields for your item here like:
    title = sc.Field()
    link = sc.Field()
    author = sc.Field()

class mycsvItem(sc.Item):
    name = sc.Field()
    sex = sc.Field()
    addr = sc.Field()
    email = sc.Field()

