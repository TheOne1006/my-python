# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Lesson1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    serial_number = scrapy.Field()
    movie_name = scrapy.Field()
    introduce = scrapy.Field()
    star = scrapy.Field()
    # 评论数
    evaluate = scrapy.Field()
    # 描述
    desc = scrapy.Field()