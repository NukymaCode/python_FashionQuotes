# -*- coding: utf-8 -*-
from re import search

class CleanPipe(object):
    def process_item(self, item, spider):

        # TEXT: convert list into strings and get rid of the \n and the curved""
        str_text = ''.join(item['text'])
        clean_text = search('“(.*)”', str_text)
        item['text'] = clean_text.group(1)

        # LIKES: Convert into integer and get ride of the word "likes"
        item['likes'] = int(item['likes'].replace(" likes",""))

        # TAGS: Return a string of tags, not an array
        item['tags'] = ",".join(str(i) for i in item['tags'])

        return item
