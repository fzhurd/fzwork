#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy.selector import Selector
from relator.items import RelatorItem

# scrapy crawl relator_spider
# scrapy crawl relator_spider -o items.json -t json

class RelatorSpider(Spider):


    name = "relator_spider"

    allowed_domains = ["www.relator.ca"]


    start_urls = [
  
        "https://www.realtor.ca/Residential/Map.aspx#CultureId=1&ApplicationId=1&RecordsPerPage=9&MaximumResults=9&PropertySearchTypeId=1&TransactionTypeId=2&StoreyRange=0-0&BedRange=0-0&BathRange=0-0&LongitudeMin=-123.29681396484376&LongitudeMax=-122.96550750732423&LatitudeMin=49.11287172635217&LatitudeMax=49.20828967427575&SortOrder=A&SortBy=1&viewState=m&Longitude=-123.131160736084&Latitude=49.1606036799933&ZoomLevel=12&PropertyTypeGroupID=1"
        # "https://www.realtor.ca/"
    ]

    # allowed_domains = ["cnblogs.com"]   
    # start_urls = ['http://www.cnblogs.com/geqianst/p/',]   

    def parse(self, response):

        houses = Selector(response).xpath('/body/div[@class="m_map"]')
        # houses = Selector(response).xpath('//div')
        print houses

        for h in houses:

            item = StackworkItem()

            item['title'] = h.xpath('a[@class="question-hyperlink"]/text()').extract()[0]

            item['url'] = h.xpath('a[@class="question-hyperlink"]/@href').extract()[0]

            yield item


    # def parse(self, response):
    #     questions = response.xpath('//div[@id="myposts"]//a[@id]')
        # xpath选择器，这里的含义是取所有id为myposts的div，在它下面找所有带id的超链接a
        # 实际结果是这样的
        # [<Selector xpath='//div[@id="myposts"]//a[@id]' data=u'<a id="PostsList1_rpPosts_TitleUrl_0" hr'>,
        # <Selector xpath='//div[@id="myposts"]//a[@id]' data=u'<a id="PostsList1_rpPosts_TitleUrl_1" hr'>,
        # <Selector xpath='//div[@id="myposts"]//a[@id]' data=u'<a id="PostsList1_rpPosts_TitleUrl_2" hr'>,
        # <Selector xpath='//div[@id="myposts"]//a[@id]' data=u'<a id="PostsList1_rpPosts_TitleUrl_3" hr'>,
        # <Selector xpath='//div[@id="myposts"]//a[@id]' data=u'<a id="PostsList1_rpPosts_TitleUrl_4" hr'>,
        # <Selector xpath='//div[@id="myposts"]//a[@id]' data=u'<a id="PostsList1_rpPosts_TitleUrl_5" hr'>,
        # <Selector xpath='//div[@id="myposts"]//a[@id]' data=u'<a id="PostsList1_rpPosts_TitleUrl_6" hr'>,
        # <Selector xpath='//div[@id="myposts"]//a[@id]' data=u'<a id="PostsList1_rpPosts_TitleUrl_7" hr'>,
        # <Selector xpath='//div[@id="myposts"]//a[@id]' data=u'<a id="PostsList1_rpPosts_TitleUrl_8" hr'>,
        # <Selector xpath='//div[@id="myposts"]//a[@id]' data=u'<a id="PostsList1_rpPosts_TitleUrl_9" hr'>]
        #
        # for question in questions:
        #     item = RelatorItem()
        #     item['title'] = question.xpath(
        #         'text()').extract()[0]
        #     item['url'] = question.xpath(
        #         '@href').extract()[0]
        #     print item
        #     yield item

        # questions = Selector(response).xpath('//div[@class="summary"]/h3')

        # for question in questions:

        #     item = StackworkItem()

        #     item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]

        #     item['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]

        #     yield item