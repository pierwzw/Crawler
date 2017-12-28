# -*- coding: utf-8 -*-
import scrapy
import re
import json
from Crawler.items import goodsItem, commentItem
from scrapy.http import Request


class JdHomeSpider(scrapy.Spider):
    name = 'jd_home'
    # allowed_domains = []
    start_urls = []
    for i in range(1, 3):
        url = 'https://list.jd.com/list.html?cat=670,671,672&page=' + str(i) + \
              '&sort=sort%5Ftotalsales15%5Fdesc&trans=1&JL=6_0_0#J_main'
        start_urls.append(url)

    def parse(self, response):
        """
        解析搜索页
        :param response:
        :return:
        """

        goods = response.xpath('//li[@class="gl-item"]')
        for good in goods:
            #千万不能放for循环外，不然只会获取每页的第一个商品
            item = goodsItem()
            item['ID'] = good.xpath('./div/@data-sku').extract()
            item['name'] = good.xpath('./div/div[@class="p-name"]/a/em/text()').extract()
            # 找不到
            item['shop_name'] = good.xpath('./div/div[@class="p-shop"]/@data-shop_name').extract()
            item['link'] = good.xpath('./div/div[@class="p-img"]/a/@href').extract()
            # "#comments-list"??  [0]??
            url = 'http:' + item['link'][0] + '#comments-list'
            #yield item
            yield Request(url, meta={'itemkey': item}, callback=self.parse_detail)

    def parse_detail(self, response):
        """
        解析详情页
        :param response:
        :return:
        """

        item = response.meta['itemkey']
        temp = str(response.body).split('commentVersion:')
        pattern = re.compile("[\'](\d+)[\']")
        if len(temp) < 2:
            item['commentVersion'] = -1
        else:
            #item['commentVersion'] = pattern.match(temp[1][:10]).group()
            item['commentVersion'] = pattern.findall(temp[1][:10].replace('\\',''))

        url = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds=' + str(item['ID'][0])
        yield Request(url, meta={'itemkey': item}, callback=self.parse_getCommentnum)
        #yield item

    def parse_getCommentnum(self, response):
        """
        解析评论数
        :param response:
        :return:
        """

        item = response.meta['itemkey']
        #windows下用gbk，用utf-8会出错
        js = json.loads(response.body.decode('gbk'))
        #print(js)
        item['comment_count'] = js['CommentsCount'][0]['CommentCount']
        item['good_comment_count'] = js['CommentsCount'][0]['GoodCount']
        item['general_comment_count'] = js['CommentsCount'][0]['GeneralCount']
        item['poor_comment_count'] = js['CommentsCount'][0]['PoorCount']
        item['average_score'] = js['CommentsCount'][0]['AverageScore']

        url = 'https://p.3.cn/prices/mgets?type=1&pdtk=&pdpin=&pin=null&pdbp=0&skuIds=J_' + str(item['ID'][0])
        yield Request(url, meta={'itemkey': item}, callback=self.parse_price)
        #yield item

    def parse_price(self, response):
        """
        解析价格
        :param response:
        :return:
        """

        item = response.meta['itemkey']
        #windows下为gbk
        jsonstr = re.sub(re.compile('[\[|\]]'), '', response.body.decode('gbk'))
        #print(jsonstr)
        js = json.loads(jsonstr)
        item['price'] = js['p']
        yield item
