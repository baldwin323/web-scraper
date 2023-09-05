```python
from flask import Flask, render_template, request
from web_scraper.reddit_scraper import WebScraper

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        search_criteria = request.form.get('search_criteria')
        
        # Triggering the web scraping process
        web_scraper = WebScraper()
        web_scraper.start_urls = [search_criteria]
        web_scraper.parse()
        
        return 'Scraping process initiated.'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
```
This file creates a simple Flask UI where users can enter the website they want to scrape in a form. When the form is submitted, it triggers the web scraping process for the entered website. The UI renders a simple HTML form in 'form.html'. The HTML file should be in a templates folder in your project directory, and looks like this:

```html
<form method="POST">
    <label for="search_criteria">Enter a website to scrape:</label><br>
    <input type="text" id="search_criteria" name="search_criteria"><br>
    <input type="submit" value="Submit">
</form>
```

Although this is a very simple UI, this would be a good starting point if you want to build a more complex web interface for your web scraper.