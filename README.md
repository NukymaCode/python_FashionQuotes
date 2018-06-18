# python_FashionQuotes

Python Scrapy spider - Scrapes fashion quote info through goodreads . com. It also download all the quote's author images.

To run this spider: scrapy crawl quotes

To change the data format: settings.py

  #Change this lines:
  FEED_FORMAT = 'json'
  FEED_URI = './output/data/quotes_%(time)s.json'
  
  #To this other lines:
  FEED_FORMAT = 'csv'
  FEED_URI = './output/data/quotes_%(time)s.csv'
