# -*- coding: utf-8 -*-
class DefaultImagePipe(object):

    def process_item(self, item, spider):
        # IMAGE: If a quote doesn't have image, a default one is picked
        if item['image_urls'] == [None]:
            item['image_urls'] = ['https://www.shareicon.net/data/48x48/2016/08/06/807595_triangle_512x512.png']

        return item
