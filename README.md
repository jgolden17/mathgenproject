# mathgenproject
> Mathematics Genealogy Project Spider

A webspider for the [Mathematics Genealogy Project](https://genealogy.math.ndsu.nodak.edu/index.php).

## Installation

Use the package manager pip to install the spider.

```bash
pip install mathgenproject-jgolden17
```

## Usage

Define a pipeline through which to process each mathematician returned from the spider.

```python
class MyPipeline(object):
    def open_spider(self, spider):
        ...

    def process_item(self, item, spider):
        print(item['name'])
        return item

    def close_spider(self, spider):
        ...

```

Run the spider using scrapy's `CrawlerProcess`, passing in the mathematician's MGP ID.

```python
from scrapy.crawler import CrawlerProcess
from mathgenproject.spiders import MathGenProjectSpider

process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'items.json',
    'ITEM_PIPELINES': {
        'MyPipeline': 300,
    },
})

process.crawl(MathGenProjectSpider, mgp_id='216087')
process.start()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
