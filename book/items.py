# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    _id = scrapy.Field()               # ID
    name = scrapy.Field()              # 书名
    commit = scrapy.Field()            # 评价数
    author = scrapy.Field()            # 作者
    fixed_price = scrapy.Field()       # 码洋（定价）
    discounted_price = scrapy.Field()  # 实洋（京东价）
    publisher = scrapy.Field()         # 出版社
    ISBN = scrapy.Field()              # ISBN
    edition = scrapy.Field()           # 版次
    jd_id = scrapy.Field()             # 京东ID
    pack_type = scrapy.Field()         # 包装（精装、平装）
    paper_type = scrapy.Field()        # 纸张（胶版纸）
    paper_size = scrapy.Field()        # 开本
    page_count = scrapy.Field()        # 页数
    word_count = scrapy.Field()        # 字数
    high_opinion = scrapy.Field()      # 好评率
    middle_opinion = scrapy.Field()    # 中评率
    low_opinion = scrapy.Field()       # 差评率
    tags = scrapy.Field()              # 标签
    publish_date = scrapy.Field()      # 出版时间
    classify = scrapy.Field()          # 京东书本分类
