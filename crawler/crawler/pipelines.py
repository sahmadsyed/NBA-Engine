class crawlerPipeline(object):
    """
    Saves player id model in DB.

    """
    def process_item(self, item, spider):
        """
        Saves scraped player id.

        Args:
            item (object): PlayerIdItem instance of scraped player id
            spider (object): Spider which scraped player id

        Returns:
            object: PlayerIdItem instance with scraped player id
        """

    	item.save()
        return item
