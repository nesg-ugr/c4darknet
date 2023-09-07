# -*- coding: utf-8 -*-

# Scrapy settings for i2p project
#
# For simplicity, this file contains only settings considered important or
# commonly used. More settings and their documentation in:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import settings

BOT_NAME = 'darknet'

SPIDER_MODULES = ['darknet.spiders']
NEWSPIDER_MODULE = 'darknet.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'darknet (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = settings.HTTP_TIMEOUT
RETRY_TIMES = settings.MAX_CRAWLING_ATTEMPTS_ON_ERROR
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'darknet.middlewares.DarknetSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'darknet.middlewares.DarknetProxyMiddleware': 200,
    'darknet.middlewares.DarknetFilterMiddleware': 300,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'darknet.pipelines.DarknetPipeline': 300,
}

# The maximum depth that will be allowed to crawl for any site:
DEPTH_LIMIT = 3

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#FEED_STORAGES_BASE = {
#    '': 'darknet.exportutils.CustomFileFeedStorage',
#    'file': 'i2darknetp.exportutils.CustomFileFeedStorage'
#}

# CUSTOM CONFIGURATION
PATH_ONGOING_SPIDERS="/home/administrador/datos/freenet/spiders/ongoing/"
PATH_FINISHED_SPIDERS="/home/administrador/datos/freenet/spiders/finished/"
PATH_LOG='/home/administrador/datos/freenet/logs/'
PATH_DATA='../data/'