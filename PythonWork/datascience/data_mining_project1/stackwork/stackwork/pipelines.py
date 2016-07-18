# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
 
from scrapy.conf import settings

from scrapy.exceptions import DropItem
from scrapy import log
 
 
class MongoDBPipeline(object):
 
    def __init__(self):

        connection = pymongo.Connection(settings['MONGODB_SERVER'],settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        # self.server = settings['MONGODB_SERVER']
        # self.port = settings['MONGODB_PORT']
        # self.db = settings['MONGODB_DB']
        # self.col = settings['MONGODB_COLLECTION']
        # connection = pymongo.Connection(self.server, self.port)
        # db = connection[self.db]
        # self.collection = db[self.col]


class StackworkPipeline(object):

    # def process_item(self, item, spider):
    #     return item

	def process_item(self, item, spider):
	    valid = True
	    for data in item:
	        if not data:
	            valid = False
	            raise DropItem("Missing {0}!".format(data))
	    if valid:
	        self.collection.insert(dict(item))
	        log.msg("Question added to MongoDB database!",
	                level=log.DEBUG, spider=spider)
	    return item

    # self.collection.insert(dict(item))
    # log.msg('Item written to MongoDB database %s/%s' % (self.db, self.col),level=log.DEBUG, spider=spider)
    # return item
