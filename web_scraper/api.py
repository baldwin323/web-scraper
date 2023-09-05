```python
from flask import Flask, request, jsonify
from web_scraper.reddit_scraper import WebScraper

app = Flask(__name__)

@app.route('/scrape', methods=['POST'])
def scrape():
    # Retrieve website URL from the payload
    url_to_scrape = request.json.get('url')
    if not url_to_scrape: 
        return jsonify({'error': 'URL to scrape not provided'}), 400

    # Triggering the web scraping process
    web_scraper = WebScraper()
    web_scraper.start_urls = [url_to_scrape]
    web_scraper.parse()

    return jsonify({'message': 'Scraping process initiated'}), 201

if __name__ == '__main__':
    app.run(debug=True)
```
This file creates a new Flask API endpoint 'scrape' that accepts POST requests with a JSON payload containing the 'url' key. The value of this key should be the URL to scrape. When a request is made to this endpoint, it triggers the web scraping process for the entered URL. The API returns a JSON response indicating that the web scraping process has begun. If the 'url' key is not provided in the payload, the API returns an error in the response. The Flask application runs on the default host (localhost) and port (5000) and has debug mode enabled, which provides more detailed error messages.