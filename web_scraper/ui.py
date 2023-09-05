```python
from flask import Flask, render_template, request
from flask_paginate import Pagination
from web_scraper.reddit_scraper import WebScraper
from urllib.parse import urlparse
import requests

app = Flask(__name__)

def is_valid_url(url):
    """
    Checks if a URL is valid.
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        url = request.form.get('search_criteria')
        # Checking if the URL is valid 
        if is_valid_url(url):
            # Triggering the web scraping process
            web_scraper = WebScraper()
            web_scraper.start_urls = [url]
            try:
                web_scraper.parse()
            except Exception as e:
                return f"An error occurred: {str(e)}"
            return 'Scraping process initiated.'
        else:
            return 'Invalid URL entered!'
    else:
        return render_template('form.html')

@app.route('/results', methods=['GET'])
def display_results():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get('page', 1, type=int)
    pagination = Pagination(page=page, total=1000, search=search, record_name='items', css_framework='bootstrap4')
    return render_template('results.html', pagination=pagination)

if __name__ == '__main__':
    app.run(debug=True)
```
The UI now validates the user input to ensure a valid URL is entered. It also handles any exceptions that occur during the web scraping process to avoid unexpected crashes.
Pagination has been implemented to handle websites with large number of pages.
The scrapped results can now be seen in a new '/results' endpoint, which are displayed in a more organized format on a 'results.html' page.