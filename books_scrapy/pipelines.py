# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class BooksScrapyPipeline:

    def __init__(self):
        self._initialize_connection()

    def _initialize_connection(self):
        """database work"""
        self.__connect()
        self.__create_db_table()

    def __connect(self):
        """connect (or create) sqlite db"""
        self.con = sqlite3.connect('books.db')
        self.cur = self.con.cursor()
        return

    def __create_db_table(self):
        """create table"""
        self.cur.execute("DROP TABLE IF EXISTS booktable")
        self.cur.execute('create table booktable (title text, price tag)')
        return

    def __insert(self, item):
        self.cur.execute("insert into booktable values (?,?)",
                         (item["title"][0], item["price"][0]))
        self.con.commit()
        return

    def process_item(self, item, spider):
        self.__insert(item)
        return item
