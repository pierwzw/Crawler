# -*- coding: utf-8 -*-
import scrapy
from Crawler.items import CrawlerItem


class MyspiderSpider(scrapy.Spider):
    name = 'MySpider'
    #allowed_domains = ['weixin.sogou.com', 'weixin.qq.com']
    start_urls = ['http://mp.weixin.qq.com/s?src=11&timestamp=1514340457&ver='
                  '599&signature=qHhaq7uEihzaeGrC-EdSQGG66KYybQCDWptvIuII*98DH'
                  'pD0vg2YsNQbBykOQvr9l7JKLa-hEVCwhSe*gvxpXC8DO*oaQaWn3Yfr2k1dwr-Mli83-8Hw7SWPzpINv2lm&new=1',
        'http://mp.weixin.qq.com/s?src=11&timestamp=1514340457&ver=599&signature=MEOlbwIYF*phoxQdP*jSmCy'
        'KaGNxc4JB*l*n5s54oRr4HsuOTYBCTZdolDag755U2NTToo7*7XHLQZU31ZfcfD7pu28ldNpe1Vu5*p1n-Q4fQoeimkqmDqQvryTOO9q6&new=1',
        'http://mp.weixin.qq.com/s?src=11&timestamp=1514340457&ver=599&signature=rEw6YrbX9DYRufDlbhVzmXy'
        'STqU3rIyiy-8T0s1ViSPEtCriwWU*Skx-t8WNkqpDsvbo3NdCip*xLTE1Ku9ulI4bEX8WzAnGS1X7zt7eUMG2LUQx1b3757ftGWGh0qFs&new=1']

    #必须得加http://
    url2 = ['http://www.jd.com', 'http://sina.com.cn', 'http://www.baidu.com']

    def __init__(self, myurl=None, *args, **kwargs):
        """
        重写init方法，使能进行参数传递
        :param myurl:
        :param args:
        :param kwargs:
        """
        
        super(MyspiderSpider, self).__init__(*args, **kwargs)
        print('要爬取的网址为： %s' % myurl)
        #下面的为什么格式化?可以不用
        self.start_urls = myurl.split(',')

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
        item['urlname'] = response.xpath('/html/head/title/text()')
        print(item['urlname'])
