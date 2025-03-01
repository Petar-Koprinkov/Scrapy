# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        star_mapping = {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5
        }

        stars = adapter.get('stars_count')
        if stars in star_mapping:
            adapter['stars_count'] = star_mapping[stars]

        availability = adapter.get('available').split('(')
        available = availability[1]
        list_number_of_available = available.split(' ')
        number_of_available = int(list_number_of_available[0])
        adapter['available'] = number_of_available

        return item
