# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from Crawler.items import mycsvItem


class MycsvSpider(CSVFeedSpider):
    name = 'mycsv'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
    headers = ['name', 'sex', 'addr', 'email']
    delimiter = ','

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = mycsvItem()
        i['name'] = row['name'].encode()
        i['sex'] = row['sex'].encode()
        print("名字是：")
        print(i['name'])
        print("性别是：")
        print(i['sex'])
        print('--------------------------------')
        return i
