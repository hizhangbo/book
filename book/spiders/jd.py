# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy import Request
from scrapy import Spider
from items import BookItem


class JdSpider(Spider):
    name = 'jd'
    allowed_domains = ['list.jd.com']
    start_urls = [#'https://list.jd.com/list.html?cat=1713,3267&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3266&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3264&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3265&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,13613&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3270&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3271&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,9278&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,9301&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,9309&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,9314&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3269&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3272&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3273&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3279&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3275&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3274&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3277&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3280&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3281&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_7_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3284&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3287&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3285&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,9340&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,9368&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3286&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,9351&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3288&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_7_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3289&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3282&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,11047&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_7_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3290&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,3291&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  'https://list.jd.com/list.html?cat=1713,3294&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,4758&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_7_0#J_main',
                  #'https://list.jd.com/list.html?cat=1713,4855&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_7_0#J_main',
                  'https://list.jd.com/list.html?cat=1713,6929&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_10_0#J_main',
                  'https://list.jd.com/list.html?cat=1713,14669&page=1&delivery=1&sort=sort_totalsales15_desc&trans=1&JL=4_10_0#J_main',
                  'https://list.jd.com/list.html?cat=1713,3296&page=1&delivery=1&stock=0&sort=sort_rank_asc&trans=1&JL=4_7_0#J_main'
                  ]

    custom_settings = {
        # download中间件
        'DOWNLOADER_MIDDLEWARES': {
            'book.middlewares.MyCustomDownloaderMiddleware': 543,
        },

        # item处理管道
        'ITEM_PIPELINES': {
            'book.pipelines.BookPipeline': 300,
        },
    }

    url_dic = {#'3267':'励志/成功',
               #'3266':'管理',
               #'3264':'经济',
               #'3265':'金融/投资',
               #'13613':'孕教/胎教',
               #'3270':'育儿/家教',
               #'3271':'旅游/地图',
               #'9278':'烹饪/美食',
               #'9301':'家居',
               #'9309':'婚恋/两性',
               #'9314':'娱乐/休闲',
               #'3269':'健身/保健',
               #'3272':'动漫',
               #'3273':'历史',
               #'3279':'心理学',
               #'3275':'国学/古籍',
               #'3274':'哲学/宗教',
               #'3277':'法律',
               #'3280':'文化',
               #'3281':'社会科学',
               #'3284':'建筑',
               #'3287':'计算机/互联网',
               #'3285':'医学',
               #'9340':'科普',
               #'9368':'农业/林业',
               #'3286':'自然/科学',
               #'9351':'电子/通信',
               #'3288':'体育/运动',
               #'3289':'中小学教辅',
               #'3282':'工业技术',
               #'11047':'大中专教辅',
               #'3290':'考试',
               #'3291':'外语学习',
               '3294':'字典/工具书',
               #'4758':'杂志/期刊',
               #'4855':'进口原版',
               '6929':'港台图书',
               '14669':'日本图书',
               '3296':'套装书'
               }

    def parse(self, response):
        if response.status == 200:
            origin_url = response.url
            html = response.body.decode(encoding="utf-8", errors="strict")
            books = Selector(text=html).xpath('//div[@id="plist"]/ul[contains(@class, "gl-warp")]/li')

            for book in books:
                book_xpath = book.xpath('./div[contains(@class, "gl-i-wrap")]')

                name = book_xpath.xpath('./div[@class="p-name"]/a/em/text()').extract_first() # 书名
                commit = book_xpath.xpath('./div[@class="p-commit"]/strong/a/text()').extract_first() # 评价数
                detail_url = book_xpath.xpath('./div[@class="p-img"]/a/@href').extract_first() # 详情页

                # 纵向抓取(详情)
                yield Request(url='https:{}'.format(detail_url), 
                              meta={'name':name, 'commit':commit, 'origin_url':origin_url}, 
                              callback=self.parse_detail,
                              dont_filter=True)

            # 横向抓取(分页)
            next_page = response.xpath('//a[@class="pn-next"]/@href').extract_first()
            if next_page is not None:
                yield Request(url='https://list.jd.com{}'.format(next_page), 
                              callback=self.parse, 
                              dont_filter=True)

    def parse_detail(self, response):
        if response.status == 200:
            book = BookItem()
            book['name'] = response.meta['name']
            book['commit'] = response.meta['commit']
            origin_url = response.meta['origin_url']

            html = response.body.decode(encoding="utf-8", errors="strict")
            book['author'] = Selector(text=html).xpath('//div[@id="p-author"]/a[1]/text()').extract_first()
            book['fixed_price'] = Selector(text=html).xpath('//del[@id="page_maprice"]/text()').extract_first()
            book['discounted_price'] = Selector(text=html).xpath('//strong[@id="jd-price"]/text()').extract_first()

            for prop in Selector(text=html).xpath('//ul[@id="parameter2"]/li'):
                feature = prop.xpath('./text()').extract_first()
                if '出版社' in feature:
                    book['publisher'] = prop.xpath('./@title').extract_first()
                elif 'ISBN' in feature:
                    book['ISBN'] = prop.xpath('./@title').extract_first()
                elif '版次' in feature:
                    book['edition'] = prop.xpath('./@title').extract_first()
                elif '商品编码' in feature:
                    book['jd_id'] = prop.xpath('./@title').extract_first()
                elif '包装' in feature:
                    book['pack_type'] = prop.xpath('./@title').extract_first()
                elif '用纸' in feature:
                    book['paper_type'] = prop.xpath('./@title').extract_first()
                elif '开本' in feature:
                    book['paper_size'] = prop.xpath('./@title').extract_first()
                elif '页数' in feature:
                    book['page_count'] = prop.xpath('./@title').extract_first()
                elif '字数' in feature:
                    book['word_count'] = prop.xpath('./@title').extract_first()
                elif '出版时间' in feature:
                    book['publish_date'] = prop.xpath('./@title').extract_first()
                else:
                    pass
            
            # 评价数量
            comment_percent = Selector(text=html).xpath('//div[@id="comments-list"]/div[@class="mt"]/div/ul')

            book['high_opinion'] = comment_percent.xpath('./li[3]/@data-num').extract_first()
            book['middle_opinion'] = comment_percent.xpath('./li[4]/@data-num').extract_first()
            book['low_opinion'] = comment_percent.xpath('./li[5]/@data-num').extract_first()
            
            # 用户标签
            comment = Selector(text=html).xpath('//div[@id="i-comment"]')
            comment_tags = comment.xpath('./div[@class="actor-new"]/dl/dd/q')

            book['tags'] = ""
            for tag in comment_tags:
                value = tag.xpath('./span/text()').extract_first()
                count = tag.xpath('./em/text()').extract_first()
                tmp_tag = str({'value':value, 'count':count})
                book['tags'] += tmp_tag + ','

            for (key,value) in self.url_dic.items():
                if key in origin_url:
                    book['classify'] = value
                    break
                
            return book
