# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        stars = adapter.get('stars')

        if stars == "zero":
            adapter['stars'] = 0
        elif stars == "one":
            adapter['stars'] = 1
        elif stars == "two":
            adapter['stars'] = 2
        elif stars == "three":
            adapter['stars'] = 3
        elif stars == "four":
            adapter['stars'] = 4
        elif stars == "five":
            adapter['stars'] = 5
