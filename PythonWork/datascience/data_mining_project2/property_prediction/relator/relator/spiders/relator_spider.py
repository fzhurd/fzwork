#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy.selector import Selector

from relator.items import RelatorItem


class StackSpider(Spider):

    name = "relator_spider"
    allowed_domains = ["www.relator.ca"]
    start_urls = [
        "https://www.realtor.ca/Commercial/Map.aspx#CultureId=1&ApplicationId=1&RecordsPerPage=9&MaximumResults=9&PropertySearchTypeId=0&TransactionTypeId=2&PropertyTypeGroupID=2&LongitudeMin=-123.30780029296876&LongitudeMax=-122.95452117919923&LatitudeMin=49.1046684354908&LatitudeMax=49.216475820806444&SortOrder=A&SortBy=1&viewState=m&CurrentPage=2",
    ]

    def parse(self, response):

        house = Selector(response).xpath('//div[@class="summary"]/h3')

        # questions = Selector(response).xpath('//div[@class="summary"]/h3')

        # for question in questions:

        #     item = StackworkItem()

        #     item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]

        #     item['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]

        #     yield item