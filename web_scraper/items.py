```python
import scrapy

class WebScraperItem(scrapy.Item):
    # fields for generic webscraping
    giveaway_name = scrapy.Field() 
    url = scrapy.Field() 
    registration_deadline = scrapy.Field() 
    entry_requirements = scrapy.Field() 
    entry_form_url = scrapy.Field() 
```

