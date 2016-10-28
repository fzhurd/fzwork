#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy.selector import Selector
from relator.items import RelatorItem


class RelatorSpider(Spider):


    name = "relator_spider"

    # start_urls = [
    #     'http://quotes.toscrape.com/page/1/',
    #     'http://quotes.toscrape.com/page/2/',
    # ]

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    allowed_domains = ["www.relator.ca"]
    start_urls = [
    # 'http://quotes.toscrape.com/page/1/',
        # "https://www.realtor.ca/Residential/Map.aspx#CultureId=1&ApplicationId=1&RecordsPerPage=9&MaximumResults=9&PropertySearchTypeId=1&TransactionTypeId=2&StoreyRange=0-0&BedRange=0-0&BathRange=0-0&LongitudeMin=-123.29681396484376&LongitudeMax=-122.96550750732423&LatitudeMin=49.140954912790704&LatitudeMax=49.18024465477734&SortOrder=A&SortBy=1&viewState=m&Longitude=-123.131160736084&Latitude=49.1606036799933&ZoomLevel=12&CurrentPage=1&PropertyTypeGroupID=1"
        # "https://www.bcit.ca"
        # "http://stackoverflow.com"
        # "https://www.realtor.ca/Residential/Map.aspx#CultureId=1&ApplicationId=1&RecordsPerPage=9&MaximumResults=9&PropertySearchTypeId=1&TransactionTypeId=2&StoreyRange=0-0&BedRange=0-0&BathRange=0-0&LongitudeMin=-123.29681396484376&LongitudeMax=-122.96550750732423&LatitudeMin=49.11287172635217&LatitudeMax=49.20828967427575&SortOrder=A&SortBy=1&viewState=m&Longitude=-123.131160736084&Latitude=49.1606036799933&ZoomLevel=12&PropertyTypeGroupID=1"
        "https://www.realtor.ca/"
        # "https://www.realtor.ca/Commercial/Map.aspx#CultureId=1&ApplicationId=1&RecordsPerPage=9&MaximumResults=9&PropertySearchTypeId=0&TransactionTypeId=2&PropertyTypeGroupID=2&LongitudeMin=-123.30780029296876&LongitudeMax=-122.95452117919923&LatitudeMin=49.1046684354908&LatitudeMax=49.216475820806444&SortOrder=A&SortBy=1&viewState=m&CurrentPage=2",
    ]
# https://www.realtor.ca/Residential/Map.aspx#CultureId=1&ApplicationId=1&RecordsPerPage=9&MaximumResults=9&PropertySearchTypeId=1&TransactionTypeId=2&StoreyRange=0-0&BedRange=0-0&BathRange=0-0&LongitudeMin=-123.29681396484376&LongitudeMax=-122.96550750732423&LatitudeMin=49.11287172635217&LatitudeMax=49.20828967427575&SortOrder=A&SortBy=1&viewState=m&Longitude=-123.131160736084&Latitude=49.1606036799933&ZoomLevel=12&PropertyTypeGroupID=1
    def parse(self, response):

        # houses = Selector(response).xpath('//div[@class="m_map_map_cnt_lst_cnt_plchldr"]/')
        houses = Selector(response).xpath('//div')
        print houses

        for h in houses:

            item = StackworkItem()

            item['title'] = h.xpath('a[@class="question-hyperlink"]/text()').extract()[0]

            item['url'] = h.xpath('a[@class="question-hyperlink"]/@href').extract()[0]

            yield item

        # questions = Selector(response).xpath('//div[@class="summary"]/h3')

        # for question in questions:

        #     item = StackworkItem()

        #     item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]

        #     item['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]

        #     yield item