# -*- coding: utf-8 -*-
import scrapy
from Crawler.items import CrawlerItem


class MyspiderSpider(scrapy.Spider):
    name = 'MySpider'
    #allowed_domains = ['weixin.sogou.com', 'weixin.qq.com']
    start_urls = ['https://list.tmall.com/search_product.htm?cat'
                  '=50024399&s=120&sort=s&style=g&active=1&industryCatId=50024399&theme=663&type=pc#J_Filter']

    #必须得加http://
    #url2 = ['http://www.jd.com', 'http://sina.com.cn', 'http://www.baidu.com']
    #
    # def __init__(self, myurl=None, *args, **kwargs):
    #     """
    #     重写init方法，使能进行参数传递
    #     :param myurl:
    #     :param args:
    #     :param kwargs:
    #     """
    #
    #     super(MyspiderSpider, self).__init__(*args, **kwargs)
    #     print('要爬取的网址为： %s' % myurl)
    #     #下面的为什么格式化?可以不用
    #     self.start_urls = myurl.split(',')

    # def start_requests(self):
    #     """
    #     重新定义起始网址
    #     :return:
    #     """
    #
    #     for url in self.url2:
    #         yield self.make_requests_from_url(url)

    def parse(self, response):
        """
        对响应作出处理并返回处理后的数据
        也负责链接的跟进
        :param response:
        :return:
        """

        item = CrawlerItem()
        item['name'] = response.xpath("//a[@target='_blank']/@title").extract()
        item['price'] = response.xpath("//em/title").extract()
        item['link'] = response.xpath("//a[@target='_blank']/@href").extract()
        item['comnum'] = response.xpath("//em[@class='J_ReviewsCount']/text()").extract()
        #item['urlkey'] = response.xpath("//meta[@name='keywords']/@content").extract()
        return item
        #print(item['urlname'], item['urlkey'])
