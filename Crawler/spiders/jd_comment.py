# -*- coding: utf-8 -*-
import json
import scrapy
from numpy import *
from Crawler.items import commentItem


class JdCommentSpider(scrapy.Spider):
    name = 'jd_comment'
    #allowed_domains = []
    start_urls = []

    fr = open('c:\\jddata.csv', 'r', encoding='utf-8')
    arrayOLines = fr.readlines()
    numberOLines = len(arrayOLines)
    numberOCol = len(arrayOLines[0].split('\t'))
    #returnmat = zeros((numberOLines, numberOCol))
    #returnmat = [[0 for i in range(numberOCol)] for i in range(numberOLines)]
    #必须用array才支持二维切片,中文也支持
    #returnmat = tile([''], (numberOLines, numberOCol))
    returnmat = []
    for i in range(numberOLines):
        returnmat.append([])
        for j in range(numberOCol):
            returnmat[i].append(arrayOLines[i].strip().split('\t')[j])

    returnmat = array(returnmat)
    # for i in range(numberOLines):
    #     for j in range(numberOCol):
    #         returnmat[i][j] = arrayOLines[i].strip().split('\t')[j]

    rows, cols = returnmat.shape

    good_ids = returnmat[:, 1]
    comment_count = returnmat[:, 5]
    commentVersion = returnmat[:, 4]

    for i in range(rows):
        if int(comment_count[i]) % 10 == 0:
            page = int(comment_count[i]) / 10
        else:
            page = int(comment_count[i]) / 10 + 1

        for k in range(1,2):
            url = 'https://sclub.jd.com/comment/productPageComments.action?productId=' + str(
                good_ids[i]) + '&score=0&sortType=5&page=' + str(k) + '&pageSize=10&isShadowSku=0&fold=1'
            start_urls.append(url)

    def parse(self, response):
        """
        解析评论
        :param response:
        :return:
        """

        js = json.loads(response.body.decode('gbk'))
        comments = js['comments']
        items = []
        for comment in comments:
            item = commentItem()
            item['user_name'] = comment['nickname']
            item['user_ID'] = comment['id']
            item['userProvince'] = comment['userProvince']
            item['content'] = comment['content']
            item['good_ID'] = comment['referenceId']
            item['good_name'] = comment['referenceName']
            #item['data'] = comment['referenceTime']
            item['replyCount'] = comment['replyCount']
            item['score'] = comment['score']
            item['status'] = comment['status']
            title = ''
            if 'title' in comment:
                title = comment['title']
            item['title'] = title
            #item['userLevelId'] = comment['']
            item['creationTime'] = comment['creationTime']
            item['productColor'] = comment['productColor']
            #item['productSize'] = comment['productSize']
            item['userLevelName'] = comment['userLevelName']
            #item['userClientShow'] = comment['']
            item['isMobile'] = comment['isMobile']
            item['days'] = comment['days']
            tags = ''
            if 'commentTags' in comment:
                for i in comment['commentTags']:
                    tags += i['name'] + ' '
            item['commentTags'] = tags
            #为什么要转成list
            items.append(item)
        return items









