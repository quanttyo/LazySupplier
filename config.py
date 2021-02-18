import os.path
import sys

# Path auto detection, only change if it doesn't work
path = os.path.dirname(__file__)
engine = "sqlite:///test.sqlite"