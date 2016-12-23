# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from scrapy.spiders import Spider, Request
from scrapy.selector import Selector

from crawler.items import MepItem

class MepSpider(Spider):

    name = "mep"
    allowed_domains = ["mep.gov.cn"]
    start_urls = [
        'http://www.mep.gov.cn/home/pgt/xzcf/index.shtml',
        'http://www.mep.gov.cn/home/pgt/xzcf/index_1.shtml',

        'http://www.mep.gov.cn/home/pgt/zfxx/index.shtml',
        'http://www.mep.gov.cn/home/pgt/zfxx/index_1.shtml',
        'http://www.mep.gov.cn/home/pgt/zfxx/index_2.shtml',
        'http://www.mep.gov.cn/home/pgt/zfxx/index_3.shtml',
        'http://www.mep.gov.cn/home/pgt/zfxx/index_4.shtml'
    ]

    def parse(self, response):

        items = []
        main_rt_list = response.css('div.main_rt_list')[0]
        for data in main_rt_list.css('ul li'):
            item = MepItem()
            item['type'] = response.css('title::text').extract_first()
            item['time'] = data.css("span::text").extract_first()
            item['href'] = data.css("a::attr(href)").extract_first().replace("../../../", "")
            item['title'] = data.css("a::text").extract_first()
            items.append(item)

        return items
