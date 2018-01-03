# -*- coding: utf-8 -*-
import scrapy
import re
from Crawler.items import QiantuItem
from scrapy.http import Request


class QiantuSpider(scrapy.Spider):
    name = 'qiantu'
    allowed_domains = ['58pic.com']
    start_urls = ['http://58pic.com/tb']

    def parse(self, response):
        item = QiantuItem()
        paturl = "(http://pic.qiantucdn.com/58pic/.*?).jpg"
        item['picurl'] = re.compile(paturl).findall(str(response.body))
        patlocal = "http://pic.qiantucdn.com/58pic/.*?/.*?/.*?/(.*?).jpg"
        item['picid'] = re.compile(patlocal).findall(str(response.body))
        yield item
        for i in range(1, 200):
            nexturl = "http://www.58pic.com/piccate/3-0-0-"+str(i)+".html"
            yield Request(nexturl, callback=self.parse)
