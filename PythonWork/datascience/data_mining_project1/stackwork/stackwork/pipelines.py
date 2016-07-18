# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
 
from scrapy.conf import settings

from scrapy.exceptions import DropItem
from scrapy import log
 
 
# class MongoDBPipeline(object):
 
#     def __init__(self):

#         connection = pymongo.MongoClient(settings['MONGODB_SERVER'],settings['MONGODB_PORT'])
#         db = connection[settings['MONGODB_DB']]
#         self.collection = db[settings['MONGODB_COLLECTION']]
#         # self.server = settings['MONGODB_SERVER']
#         # self.port = settings['MONGODB_PORT']
#         # self.db = settings['MONGODB_DB']
#         # self.col = settings['MONGODB_COLLECTION']
#         # connection = pymongo.Connection(self.server, self.port)
#         # db = connection[self.db]
#         # self.collection = db[self.col]


# class StackworkPipeline(object):

#     # def process_item(self, item, spider):
#     #     return item

# 	def process_item(self, item, spider):
# 	    valid = True
# 	    for data in item:
# 	        if not data:
# 	            valid = False
# 	            raise DropItem("Missing {0}!".format(data))
# 	    if valid:
# 	        self.collection.insert(dict(item))
# 	        log.msg("Question added to MongoDB database!",
# 	                level=log.DEBUG, spider=spider)
# 	    return item

#     # self.collection.insert(dict(item))
#     # log.msg('Item written to MongoDB database %s/%s' % (self.db, self.col),level=log.DEBUG, spider=spider)
#     # return item


import json

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class MongoDBPipeline(object):

    collection_name = 'questions'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGODB_SERVER'),
            mongo_db=crawler.settings.get('MONGODB_DB', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item
