from pytest import *
import sys
import os
# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from markdown import headers

def test_headers():
    #test headers
    # Markdown: # header 1
    # HTML: <h1>header 1</h1>
    assert headers.convert('') == ''
    assert headers.convert('# header 1') == '<h1>header 1</h1>'
    assert headers.convert('## header 2') == '<h2>header 2</h2>'
    assert headers.convert('### header 3') == '<h3>header 3</h3>'
    assert headers.convert('#### header 4') == '<h4>header 4</h4>'
    assert headers.convert('##### header 5') == '<h5>header 5</h5>'
    assert headers.convert('###### header 6') == '<h6>header 6</h6>' 
