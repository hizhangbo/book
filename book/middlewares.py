# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from book.settings import USER_AGENT_LIST
from selenium.common.exceptions import TimeoutException
from scrapy.exceptions import IgnoreRequest
from selenium.webdriver.common.action_chains import ActionChains

class BookSpiderMiddleware(object):
    """
    SPIDER_MIDDLEWARES
    """
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).

        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MyCustomDownloaderMiddleware(object):
    def __init__(self):
        # self.driver = webdriver.Chrome(executable_path='E:/driver/chromedriver.exe')
        self.driver = webdriver.Firefox(executable_path='E:/driver/geckodriver.exe')
        
        # cap = webdriver.DesiredCapabilities.PHANTOMJS
        # cap["phantomjs.page.settings.resourceTimeout"] = 10000
        # cap["phantomjs.page.settings.loadImages"] = False
        # cap["phantomjs.page.settings.disk-cache"] = True
        # cap["phantomjs.page.settings.userAgent"] = (random.choice(USER_AGENT_LIST))
        # cap["phantomjs.page.customHeaders.Cookie"] = '3AB9D23F7A4B3C9B=WW7FASJ7UKIPOXM5YCOD3HNTC47Y3UXYHN23BZP26KDKHYHEKD5KNY6O2DMAWUSD2AFHGEVAY5I7W2MIR7Z3S3XF2Q;user-key=7d130e35-7b4c-4b9c-b154-9a97daf89531'
        # self.driver = webdriver.PhantomJS(executable_path='E:/driver/phantomjs.exe', desired_capabilities=cap)
        # self.driver.implicitly_wait(10)

        self.timeoutRequest = {}
    """
    DOWNLOADER_MIDDLEWARES
    """
    def process_request(self, request, spider):
        try:
            self.driver.set_page_load_timeout(10)
            self.driver.get(request.url)
            # self.driver.maximize_window()
        except TimeoutException as e:
            pass

        # 详情页动态加载
        if 'item.jd.com' in request.url:
            comment = self.driver.find_element_by_id('comment')
            if comment is not None:
                js = '''
                    　　function getElementViewTop(element){ 
                    　　　　var actualTop = element.offsetTop; 
                    　　　　var current = element.offsetParent; 

                    　　　　while (current !== null){ 
                    　　　　　　actualTop += current. offsetTop; 
                    　　　　　　current = current.offsetParent; 
                    　　　　} 

                    　　　　 if (document.compatMode == "BackCompat"){ 
                    　　　　　　var elementScrollTop=document.body.scrollTop; 
                    　　　　} else { 
                    　　　　　　var elementScrollTop=document.documentElement.scrollTop; 
                    　　　　} 

                    　　　　return actualTop-elementScrollTop; 
                    　　}
                        comment = document.getElementById("comment")
                        var q=document.documentElement.scrollTop=getElementViewTop(comment)
                '''
                self.driver.execute_script(js)
            else:
                js = "var q=document.documentElement.scrollTop=100000"
                self.driver.execute_script(js)

            time.sleep(2)
            # 解决部分请求超时的问题（动态页面滚动出发ajax请求，但页面长度不一）
            # if request.url in self.timeoutRequest.keys():
            #     time.sleep(1)

            try:
                WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.CLASS_NAME,'comments-item'))
                )
            except TimeoutException as e:
                if request.url in self.timeoutRequest.keys():
                    self.timeoutRequest[request.url] += 1
                else:
                    self.timeoutRequest[request.url] = 1
                if self.timeoutRequest[request.url] < 3:
                    return request
                else:
                    with open('requestTimeout.txt', 'a', encoding='utf-8') as out:
                        out.write(str.format('{}\r\n', request.url))
                    raise IgnoreRequest("Ignored request not in cache: %s" % request)
            # comment = self.driver.find_elements_by_id('comments-list')
            # if comment is None:
            #     js_again = "var q=document.documentElement.scrollTop=-10"
            #     self.driver.execute_script(js_again)
                
            # time.sleep(5)
        
        content = self.driver.page_source.encode('utf-8')
        
        return HtmlResponse(request.url, request=request, encoding='utf-8', body=content)
        # raise IgnoreRequest("Ignored request not in cache: %s" % request)

    def process_response(self, request, response, spider):
        spider.logger.info('process_response: %s' % spider.name)
        return response

    def process_exception(self, request, exception, spider):
        with open('error.txt', 'a', encoding='utf-8') as log:
            log.writelines(str(exception))
        return None

    def __del__(self):
        self.driver.quit()
