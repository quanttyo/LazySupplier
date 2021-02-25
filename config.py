import os.path

# Path auto detection, only change if it doesn't work
app = 'supp_tool'
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
path = os.path.dirname(__file__)
cache = os.path.join(path, 'cache')
assets = os.path.join(path, 'assets')
engine = "sqlite:///test.sqlite3"


class Config:
    app = 'supp_tool'
    LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
    path = os.path.dirname(__file__)
    cache = os.path.join(path, 'cache')
    assets = os.path.join(path, 'assets')
    engine = "sqlite:///test.sqlite3"
    ex_params = {'headers': {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) '
                      'Gecko/20100101 Firefox/45.0'},
        'url': 'https://www.wildberries.ru/catalog/{}/detail.aspx',
        'class': 'preview-photo j-zoom-preview'
    }
