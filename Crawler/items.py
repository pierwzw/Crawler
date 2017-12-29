# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class CrawlerItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    price = Field()
    link = Field()
    comnum = Field()


class myXmlItem(Item):
    # define the fields for your item here like:
    title = Field()
    link = Field()
    author = Field()


class mycsvItem(Item):
    name = Field()
    sex = Field()
    addr = Field()
    email = Field()


class autoItem(Item):
    name = Field()
    price = Field()
    link = Field()
    comnum = Field()


class goodsItem(Item):
    name = Field()
    price = Field()
    link = Field()
    comment_count = Field()
    ID = Field()
    shop_name = Field()
    average_score = Field()
    good_comment_count = Field()
    general_comment_count = Field()
    poor_comment_count = Field()
    commentVersion = Field()
    #为了得到评论的地址需要该字段
    # score1count = Field()     # 评分为1星的人
    # score2count = Field()     # 评分为2星的人
    # score3count = Field()     # 评分为3星的人
    # score4count = Field()     # 评分为4星的人
    # score5count = Field()     # 评分为5星的人


class commentItem(Item):
    user_name = Field()
    user_ID = Field()
    userProvince = Field()
    content = Field()
    good_ID = Field()
    good_name = Field()
    replyCount = Field()
    score = Field()
    status = Field()
    title = Field()
    userLevelId = Field()
    creationTime = Field()  # 用户注册时间
    productColor = Field()  # 商品颜色
    productSize = Field()  # 商品大小
    userLevelName = Field()  # 银牌会员，钻石会员等
    userClientShow = Field()  # 来自什么 比如来自京东客户端
    isMobile = Field()  # 是否来自手机
    days = Field()  # 天数
    commentTags = Field()  # 标签

