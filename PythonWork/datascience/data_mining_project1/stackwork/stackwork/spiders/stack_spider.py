#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy.selector import Selector

from stackwork.items import StackworkItem


# scrapy crawl stack_spider
 
 
class StackSpider(Spider):
    name = "stack_spider"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

    def parse(self, response):

        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:

            item = StackworkItem()

            item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]

            item['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]

            yield item