BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawler (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
	'crawler.pipelines.crawlerPipeline': 1
}

import sys
sys.path.insert(0, '/home/salman/nba_engine')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'nba_engine.settings'
