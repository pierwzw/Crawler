# -*- coding: utf-8 -*-
import scrapy


class MyhexunSpider(scrapy.Spider):
    name = 'myhexun'
    allowed_domains = ['hexun.com']
    start_urls = ['http://hexun.com/']

    def parse(self, response):
        pass
