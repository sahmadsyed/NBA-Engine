BOT_NAME = 'nbaCrawler'

SPIDER_MODULES = ['nbaCrawler.spiders']
NEWSPIDER_MODULE = 'nbaCrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'nbaCrawler (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
	'nbaCrawler.pipelines.NbacrawlerPipeline': 1
}

import sys
sys.path.insert(0, '/Users/Salman/NBAAPP/nbaApp')
sys.path.insert(0, '/Users/Salman/NBAAPP/nbaCrawler')


import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'nbaApp.settings'