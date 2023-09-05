```python
import scrapy

class AppleGiveawayScraperItem(scrapy.Item):
    # changed fields to match apple/mac/developer cpu giveaway contest data
    giveaway_name = scrapy.Field() # the specific name of the competition/giveaway
    url = scrapy.Field() # url to the webpage for the competition/giveaway
    registration_deadline = scrapy.Field() # deadline for contest entry
    entry_requirements = scrapy.Field() # information about eligibility or entry requirements
    entry_form_url = scrapy.Field() # if a form needs to be filled out, the URL for it
```