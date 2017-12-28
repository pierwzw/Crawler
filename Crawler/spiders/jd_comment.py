# -*- coding: utf-8 -*-
import scrapy


class JdCommentSpider(scrapy.Spider):
    name = 'jd_comment'
    allowed_domains = ['[]']
    start_urls = ['http://[]/']

    def parse(self, response):
        pass
