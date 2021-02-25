import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlopen
from io import BytesIO
from itertools import chain
from pickle import load, dumps, HIGHEST_PROTOCOL
from config import Config
from typing import Union


class Extractor(object):
    _image = None
    _content = None

    def __init__(self, target):
        if not os.path.exists(Config.cache):
            os.mkdir(Config.cache)

        if os.path.exists(os.path.join(Config.cache, f'{target}.jpg')):
            self._image = os.path.join(Config.cache, f'{target}.jpg')
            self._content = f'{Config.cache}/{target}.pickle'
        else:
            r = BeautifulSoup(
                requests.get(Config.ex_params['url'].format(target),
                             Config.ex_params['headers']).text,
                features='html.parser')
            if self.item_image(r):
                self._content = open(f'{Config.cache}/{target}.pickle', 'wb+')
                self._content.write(dumps(self.get_item_attributes(r),
                                          protocol=HIGHEST_PROTOCOL))
                self._content = self._content.name

                self._image = open(f'{Config.cache}/{target}.jpg', 'wb+')
                self._image.write(
                    BytesIO(urlopen(self.item_image(r)).read()).getbuffer())
                self._image = self._image.name
            else:
                self._image = f'{Config.assets}/placeholder.jpg'
                self._content = None

    @staticmethod
    def item_image(content) -> Union[str, bool]:
        image = content.find('img', {'class': Config.ex_params['class']})
        return f'http:{image["src"]}' if image else False

    @staticmethod
    def get_item_attributes(content: BeautifulSoup) -> dict:
        value = content.find('div', {
            'class': 'j-add-info-section '
                     'collapsable-content'}).find_all('div', {'class': 'pp'})
        filtered = list(filter(None,
                               chain(*[item.get_text()
                                     .split('\n') for item in
                                       value])))
        return dict(zip(filtered[::2], filtered[1::2]))

    @property
    def image(self) -> str:
        return self._image

    @property
    def content(self) -> dict:
        with open(self._content, 'rb') as handle:
            return load(handle)

    def __repr__(self):
        return f'{self._image, self._content}'
