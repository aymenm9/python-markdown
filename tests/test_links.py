from pytest import *
import sys
import os

# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from markdown import links


def test_links():
    assert links.convert('[link](https://www.google.com)') == '<a href="https://www.google.com">link</a>'