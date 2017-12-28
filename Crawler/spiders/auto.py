# -*- coding: utf-8 -*-
import scrapy
from Crawler.items import autoItem
from scrapy.http import Request


class AutoSpider(scrapy.Spider):
    name = 'auto'
    #allowed_domains = ['tmall.com']
    start_urls = ['https://list.jd.com/list.html?cat=670,671,672&page=1&sort=sort%5Ftotalsales15%5Fdesc&trans=1&JL=6_0_0#J_main']

    def parse(self, response):
        item = autoItem()
        # item['name'] = response.xpath("//a[@target='_blank']/@title").extract()
        # item['price'] = response.xpath("//em/title").extract()
        # item['link'] = response.xpath("//a[@target='_blank']/@href").extract()
        # item['comnum'] = response.xpath("//em[@class='J_ReviewsCount']/text()").extract()

        item['name'] = response.xpath("//div[@class='p-name']/a/em/text()").extract()
        item['price'] = response.xpath("//div[@class='p-price']/strong/i/text()").extract()

        item['link'] = ['https:'+price for price in response.xpath("//div[@class='p-name']/a/@href").extract()]
        item['comnum'] = response.xpath("//div[@class='tab-main']/ul/li[@data-anchor='#comment']/s/text()").extract()

        yield item

        for i in range(1, 2):
            # url = 'https://list.tmall.com/search_product.htm?cat=50024399&s='+str(i*60)+\
            #       '&sort=s&style=g&active=1&industryCatId=50024399&theme=663&type=pc#J_Filter'
            url = 'https://list.jd.com/list.html?cat=670,671,672&page='+str(i)+'&sort=sort%5Ftotalsales15%5Fdesc&trans=1&JL=6_0_0#J_main'
            yield Request(url, callback=self.parse)



