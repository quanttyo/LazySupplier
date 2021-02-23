import requests
import bs4
import os
from config import cache
from urllib.request import urlopen
from io import BytesIO
import threading

settings = {'headers': {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) '
                  'Gecko/20100101 Firefox/45.0'},
    'url': 'https://www.wildberries.ru/catalog/{}/detail.aspx',
    'class': 'preview-photo j-zoom-preview'
}


class Extractor(object):
    _image = None
    _content = None

    def __init__(self, target):
        if not os.path.exists(cache):
            os.mkdir(cache)

        if os.path.exists(os.path.join(cache, f'{target}.jpg')):
            self._image = os.path.join(cache, f'{target}.jpg')
            self._content = open(f'{cache}/{target}.content', 'r')
        else:
            r = bs4.BeautifulSoup(requests.get(settings['url'].format(target),
                                               settings['headers']).text,
                                  features='html.parser')
            self._content = open(f'{cache}/{target}.content', 'w+')
            self._image = open(f'{cache}/{target}.jpg', 'wb+')
            self._content.write(str([str(x) for x in
                                     self.get_item_attributes(r)]))
            self._image.write(BytesIO(urlopen(
                self.item_image(r)).read()).getbuffer())
            self._image = self._image.name


    def item_image(self, content):
        return f"http:{content.find('img', {'class': settings['class']})['src']}"

    def get_item_attributes(self, content):
        return content.find('div', {
            'class': 'j-add-info-section collapsable-content'})

    @property
    def image(self):
        return self._image

    @property
    def content(self):
        return self._content.read()

    def __repr__(self):
        return f'{self._image, self._content}'
