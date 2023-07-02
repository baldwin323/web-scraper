```python
import scrapy
from scrapy.crawler import CrawlerProcess
from web_scraper.spiders.reddit_spider import RedditSpider
from web_scraper.items import RedditScraperItem
from web_scraper.pipelines import JsonWriterPipeline

class RedditScraper(scrapy.Spider):
    name = "reddit_scraper"
    start_urls = ['http://www.reddit.com']

    def parse(self, response):
        for post in response.css('div.thing'):
            item = RedditScraperItem()
            item['title'] = post.css('p.title a::text').get()
            item['url'] = post.css('p.title a::attr(href)').get()
            item['upvotes'] = post.css('div.score.unvoted::attr(title)').get()
            yield item

        next_page = response.css('span.next-button a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

if __name__ == "__main__":
    process = CrawlerProcess(settings={
        'ITEM_PIPELINES': {'web_scraper.pipelines.JsonWriterPipeline': 1},
    })
    process.crawl(RedditSpider)
    process.start()
```