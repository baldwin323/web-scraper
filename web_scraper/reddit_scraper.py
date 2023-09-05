```python
import scrapy
from scrapy.crawler import CrawlerProcess
from web_scraper.spiders.reddit_spider import RedditSpider
from web_scraper.items import RedditScraperItem
from web_scraper.pipelines import JsonWriterPipeline

class RedditScraper(scrapy.Spider):
    name = "giveaway_contest_scraper"
    start_urls = ['http://www.apple.com/giveaway', 'http://www.developer.com/giveaway', 'http://www.mac.com/giveaway'] # insert actual giveaway or contest websites

    def parse(self, response):
        for post in response.css('div.thing'): #this div.thing needs to be updated to match actual CSS element of the webpages
            item = RedditScraperItem()
            item['giveaway_name'] = post.css('p.title a::text').get() # update CSS selectors to match actual CSS element
            item['url'] = post.css('p.title a::attr(href)').get() # update CSS selectors to match actual CSS element
            item['registration_deadline'] = post.css('div.deadline.unvoted::attr(date)').get() # update CSS selectors to match actual CSS element
            item['entry_requirements'] = post.css('div.info.unvoted::attr(desc)').get() # update CSS selectors to match actual CSS element
            item['entry_form_url'] = post.css('div.form.unvoted::attr(href)').get() # update CSS selectors to match actual CSS element
            yield item

        next_page = response.css('span.next-button a::attr(href)').get() # update to correctly follow pagination if any
        if next_page is not None:
            yield response.follow(next_page, self.parse)

if __name__ == "__main__":
    process = CrawlerProcess(settings={
        'ITEM_PIPELINES': {'web_scraper.pipelines.JsonWriterPipeline': 1},
    })
    process.crawl(RedditSpider)
    process.start()
```
Note that since the actual URLs and CSS selectors used in the code depend on the specific structure and URLs of the websites you're scraping, you would need to modify the 'start_urls' list and the CSS selectors in the parse method to match the actual websites and their structures.