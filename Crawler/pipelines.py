# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 导入codecs模块直接进行解码
import codecs
import json


class CrawlerPipeline(object):
    def __init__(self):
        self.file = codecs.open('c:\\jddata.csv', 'wb', encoding='utf-8')
        # self.file = open('c:\\jddata.csv', 'wb')

    def process_item(self, item, spider):
        # ensure_ascii=False防止中文变成二进制
        # jsonstr = json.dumps(dict(item), ensure_ascii=False)
        name = str(item['name'][0]).strip()
        ID = str(item['ID'][0])
        link = str(item['link'][0])
        shop_name = str(item['shop_name'])
        commentVersion = str(item['commentVersion'])
        comment_count = str(item['comment_count'])
        good_comment_count = str(item['good_comment_count'])
        general_comment_count = str(item['general_comment_count'])
        poor_comment_count = str(item['poor_comment_count'])
        average_score = str(item['average_score'])
        price = str(item['price'])

        data = name + '\t' + ID + '\t' + link + '\t' + shop_name + '\t' + commentVersion + '\t' + comment_count + \
               '\t' + good_comment_count + '\t' + general_comment_count + '\t' + poor_comment_count + '\t' \
               + average_score + '\t' + average_score + '\n'
        # print(data)
        self.file.write(data)
        return item

    def close_spider(self, spider):
        self.file.close()
