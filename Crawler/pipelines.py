# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 导入codecs模块直接进行解码
import codecs
import json
import pymysql
from urllib.request import urlretrieve


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
        commentVersion = str(item['commentVersion'][0])
        comment_count = str(item['comment_count'])
        good_comment_count = str(item['good_comment_count'])
        general_comment_count = str(item['general_comment_count'])
        poor_comment_count = str(item['poor_comment_count'])
        average_score = str(item['average_score'])
        price = str(item['price'])

        data = name + '\t' + ID + '\t' + link + '\t' + shop_name + '\t' + commentVersion + '\t' + comment_count + '\t' + good_comment_count + '\t' + general_comment_count + '\t' + poor_comment_count + '\t' + average_score + '\t' + average_score + '\t' + price
        # mat = "{:<12}\t{:<32}\t"
        self.file.write(data + '\n')
        return item

    def close_spider(self, spider):
        self.file.close()


class CommentPipeline(object):
    def __init__(self):
        self.file = codecs.open('c:\\jdcomment.csv', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        user_name = item['user_name']
        user_ID = item['user_ID']
        userProvince = item['userProvince']
        content = item['content']
        good_ID = item['good_ID']
        good_name = item['good_name']
        # date = item['date']
        replyCount = item['replyCount']
        score = item['score']
        status = item['status']
        title = item['title']
        creationTime = item['creationTime']
        productColor = item['productColor']
        # productSize = item['productSize']
        userLevelName = item['userLevelName']
        isMobile = item['isMobile']
        days = item['days']
        tags = item['commentTags']
        data = '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s' % (
        user_name, user_ID, userProvince, good_ID, replyCount, score, status, title, creationTime, productColor,
        userLevelName, isMobile, days, tags, good_name, content)
        self.file.write(data + '\n')
        return item

    def close_spider(self, spider):
        self.file.close()


class CsPipeline(object):
    t = 0

    def process_item(self, item, spider):
        CsPipeline.t += 1
        print(str(CsPipeline.t) + ' ' + item['name'][0])
        print(item['link'][0])
        print('---------------------------')
        return item


class SqlPipeline(object):
    def __init__(self):
        #一定要加charset='utf8'，也不能为'utf-8'
        self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='mypydb', charset='utf8')

    def process_item(self, item, spider):
        name = item['name'][0]
        keywd = item['keywd'][0]
        sql = "insert into mytb(title, keywd) values('" + name + "','" + keywd + "')"
        self.conn.query(sql)
        return item

    def close_spider(self, spider):
        self.conn.close()


class HexunPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='hexun', charset='utf8')

    def process_item(self):
        for j in range(len(item['name'])):
            name = item['name'][j]
            url = item['url'][j]
            hits = item['hits'][j]
            comment = item['comment'][j]

            sql = "insert into myhexun(name, url, hits, comment) values('"+name+\
                  "','"+url+"','"+hits+"','"+comment+"')"
            self.conn.query(sql)
        return item

    def close_spider(self, spider):
        self.conn.close()


class QiantuPipeline(object):
    def process_item(self, item, spider):
        for i in range(len(item['picurl'])):
            thispic = item['picurl'][i]
            trueurl = thispic + '_1024.jpg'
            localpath = 'c:\\qiantu\\' + item['picid'][i] + '.jpg'
            urlretrieve(trueurl, filename=localpath)
        return item



