# -*- coding: utf-8 -*-

# Scrapy settings for weibo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weibo'

SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#'''
DEFAULT_REQUEST_HEADERS = {
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
#'''

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'weibo.middlewares.WeiboSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'weibo.middlewares.WeiboDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'weibo.pipelines.WeiboPipeline': 300,
# }
#ITEM_PIPELINES = {
#    'weibo.pipelines.MongoPipeline': 300
#}

MONGO_URI = 'localhost' #数据库服务器地址，如IP地址：端口
MONGO_DB = 'weibo_db' #数据库名称
MONGO_COL = 'col'       #集合名称，即表名


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

FEED_EXPORT_ENCODING = 'gb18030'