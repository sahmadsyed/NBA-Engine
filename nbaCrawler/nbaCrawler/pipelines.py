class NbacrawlerPipeline(object):
    def process_item(self, item, spider):
    	if 'player_wiki' not in item:
    		item.save()
        return item
