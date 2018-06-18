# -*- coding: utf-8 -*-
from scrapy import Item, Field

class QuoteItems(Item):

    # INFO
    text = Field(type="str")
    author = Field(type="str")
    tags = Field(type="str")
    likes = Field(type="str")
    image_urls = Field()
    images = Field()


