import os.path
import sys

# Path auto detection, only change if it doesn't work
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
path = os.path.dirname(__file__)
cache = os.path.join(path, 'cache')
engine = "sqlite:///test.sqlite3"