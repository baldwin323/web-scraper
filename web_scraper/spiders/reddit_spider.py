```python
import scrapy
from web_scraper.items import RedditScraperItem

class RedditSpider(scrapy.Spider):
    name = "giveaway_contest_scraper"
    start_urls = ['http://www.apple.com/giveaway', 'http://www.developer.com/giveaway', 'http://www.mac.com/giveaway'] # insert actual giveaway or contest websites

    def parse(self, response):
        for post in response.css('div.thing'): #this div.thing needs to be replaced by the CSS selector for give away posts in the selected websites
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
```