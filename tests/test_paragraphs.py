from pytest import *
import sys
import os
# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from markdown import paragraph

def test_paragraphs():
    assert paragraph.convert('') == ''

    assert paragraph.convert('this is a paragraph') == '<p>this is a paragraph</p>'
    assert paragraph.convert('this is a **bold paragraph**') == '<p>this is a **bold paragraph**</p>'