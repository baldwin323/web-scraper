```python
import json

class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('giveaway_contests.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if 'Apple' in item['title'] or 'Mac' in item['title'] or 'Developer cpu' in item['title']:
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
        return item
```