# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from dangdang.settings import MONGOADDRESS
from dangdang.settings import MONGOPORT

class DangdangPipeline:
    def open_spider(self, spider):
        self.mongoClient= MongoClient(MONGOADDRESS,MONGOPORT)
        self.collection=self.mongoClient["dangdang"]["book"]
        self.collection.delete_many({})#清空之前数据


    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
