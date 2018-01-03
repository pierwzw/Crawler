# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Crawler.items import csItem


class CsSpider(CrawlSpider):
    """
    a spider based on crawlspider module
    逐层往下爬，永不停止若follow=True
    """

    name = 'cs'
    allowed_domains = ['sohu.com']
    start_urls = ['http://news.sohu.com/']

    rules = (
        #过滤后已经直接请求了
        Rule(LinkExtractor(allow=('.*?/n.*?shtml'), allow_domains=('sohu.com')), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        i = csItem()
        i['link'] = response.xpath('//link[@rel="canonical"]/@href').extract()
        i['name'] = response.xpath('/html/head/title/text()').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
