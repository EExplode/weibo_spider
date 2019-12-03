# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request
from urllib.parse import urlencode
from weibo.items import WeiboItem

class BasicSpider(Spider):
    name = 'basic'
    allowed_domains = ['weibo.com']
    start_urls = ['http://weibo.com/']
    base_url = 'https://s.weibo.com/weibo?'

    page = 50
    key_word = '迪丽热巴'

    '''
    custom_settings = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Connection': 'keep-alive',
        'Accept-Language': 'en',
        'Host': 's.weibo.com',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
        'Cookie': 'SINAGLOBAL=5646598010535.897.1570698209785; login_sid_t=9fee77f949390ee800f2c3f33ccb447d; cross_origin_proto=SSL; _s_tentry=www.baidu.com; Apache=9660639987195.676.1575335763748; ULV=1575335763756:11:1:1:9660639987195.676.1575335763748:1574938200245; WBtopGlobal_register_version=307744aa77dd5677; ALF=1606875262; SSOLoginState=1575339264; SUB=_2A25w4bVQDeRhGeBL7lMW9C_IyDqIHXVTlqGYrDV8PUNbmtBeLVfXkW9NRxCoOGOba0LiHjMbILrPZE8aFdWgDt64; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWE16P8AQ-pR_YzrrlYzwXr5JpX5KzhUgL.FoqfSK2NSh2Xe0q2dJLoI7DgqgpyMoe01KB4; SUHB=0A0Ze4_pd-MyxU; wvr=6; UOR=www.howtoing.com,widget.weibo.com,graph.qq.com; webim_unReadCount=%7B%22time%22%3A1575356907228%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A37%2C%22msgbox%22%3A0%7D; WBStorage=42212210b087ca50|undefined'
    }
    '''

    '''
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Connection': 'keep-alive',
        'Accept-Language': 'en',
        'Host': 's.weibo.com',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
        'Cookie': 'SINAGLOBAL=5646598010535.897.1570698209785; login_sid_t=9fee77f949390ee800f2c3f33ccb447d; cross_origin_proto=SSL; _s_tentry=www.baidu.com; Apache=9660639987195.676.1575335763748; ULV=1575335763756:11:1:1:9660639987195.676.1575335763748:1574938200245; WBtopGlobal_register_version=307744aa77dd5677; ALF=1606875262; SSOLoginState=1575339264; SUB=_2A25w4bVQDeRhGeBL7lMW9C_IyDqIHXVTlqGYrDV8PUNbmtBeLVfXkW9NRxCoOGOba0LiHjMbILrPZE8aFdWgDt64; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWE16P8AQ-pR_YzrrlYzwXr5JpX5KzhUgL.FoqfSK2NSh2Xe0q2dJLoI7DgqgpyMoe01KB4; SUHB=0A0Ze4_pd-MyxU; wvr=6; UOR=www.howtoing.com,widget.weibo.com,graph.qq.com; webim_unReadCount=%7B%22time%22%3A1575356907228%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A37%2C%22msgbox%22%3A0%7D; WBStorage=42212210b087ca50|undefined'
    }
    '''

    def start_requests(self):
        date = {'q': self.key_word, 'xsort': 'hot', 'suball': '1', 'Refer': 'g'}
        for i in range(1, self.page + 1):
            date['page'] = i
            params = urlencode(date)
            url = self.base_url + params
            # print(url)
            #yield Request(url, self.parse, headers=self.headers)
            yield Request(url, self.parse)

    def parse(self, response):
        id = response.xpath('//div[@class="card-wrap" and @action-type="feed_list_item"]//a[@class="name"]/text()').extract()
        L = len(id)
        time = response.xpath('//div[@class="card-wrap" and @action-type="feed_list_item"]//p[@class="from"]/a[1]/text()').extract()
        support = response.xpath('//div[@class="card-wrap" and @action-type="feed_list_item"]//li//em/text()').extract()
        share = response.xpath('//div[@class="card-wrap" and @action-type="feed_list_item"]//li[last()-2]/a/text()').extract()
        discuss = response.xpath('//div[@class="card-wrap" and @action-type="feed_list_item"]//li[last()-1]/a/text()').extract()

        for i in range(0, L):
            st = response.xpath('//div[@class="card-wrap" and @action-type="feed_list_item"][' + str(i+1) + ']//p[@class="txt"]//text()').extract()
            content = "".join(st).strip()
            item = WeiboItem()
            item['id'] = id[i]
            item['time'] = time[i].strip()
            item['discuss'] = discuss[i][3:]
            item['share'] = share[i][4:]
            item['support'] = support[i]
            item['content'] = content
            yield item
