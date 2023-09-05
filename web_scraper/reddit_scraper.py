```python
import scrapy
from scrapy.crawler import CrawlerProcess
from web_scraper.spiders.web_spider import WebSpider
from web_scraper.items import WebScraperItem
from web_scraper.pipelines import JsonWriterPipeline

class WebScraper(scrapy.Spider):
    name = "generic_web_scraper"
    start_urls = ['http://www.website.com'] 

    def parse(self, response):
        for post in response.css('post_css_selector'):
            item = WebScraperItem()
            item['giveaway_name'] = post.css('giveaway_name_css_selector').get() 
            item['url'] = post.css('url_css_selector').get() 
            item['registration_deadline'] = post.css('registration_deadline_css_selector').get() 
            item['entry_requirements'] = post.css('entry_requirements_css_selector').get() 
            item['entry_form_url'] = post.css('entry_form_url_css_selector').get() 
            yield item

        next_page = response.css('next_page_css_selector').get() 
        if next_page is not None:
            yield response.follow(next_page, self.parse)

if __name__ == "__main__":
    process = CrawlerProcess(settings={
        'ITEM_PIPELINES': {'web_scraper.pipelines.JsonWriterPipeline': 1},
    })
    process.crawl(WebSpider)
    process.start()
```

