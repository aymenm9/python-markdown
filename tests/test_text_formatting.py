from pytest import *
import sys
import os

# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from markdown import text_formatting


def test_text_formatting():
    # Test for text formatting all bold and italic
    # Markdown: ***Bold&Italic***
    # HTML: <strong><em>Bold</em></strong>
    assert text_formatting.convert('***Bold&Italic***') == '<strong><em>Bold&Italic</em></strong>'

    # Test for text formatting bold
    # Markdown: **Bold**
    # HTML: <strong>Bold</strong>
    assert text_formatting.convert('**Bold**') == '<strong>Bold</strong>'

    # Test for text formatting italic
    # Markdown: _Italic_
    # HTML: <em>Italic</em>
    assert text_formatting.convert('_Italic_') == '<em>Italic</em>'

    # Test for text formatting strikethrough
    # Markdown: ~~Strikethrough~~
    # HTML: <del>Strikethrough</del>
    assert text_formatting.convert('~~Strikethrough~~') == '<del>Strikethrough</del>'

    # Test for text formatting subscript
    # Markdown: ^Subscript^
    # HTML: <sub>Subscript</sub>
    assert text_formatting.convert('<sub>Subscript</sub>') == '<sub>Subscript</sub>'

    # Test for text formatting superscript
    # Markdown: ^Superscript^
    # HTML: <sup>Superscript</sup>
    assert text_formatting.convert('<sup>Superscript</sup>') == '<sup>Superscript</sup>'

    # Test for text formatting 
    # Markdown: str **bold** str _italic_ str ~~strikethrough~~ str <sub>subscript</sub> str <sup>superscript</sup>
    # HTML: str <strong>bold</strong> str <em>italic</em> str <del>strikethrough</del> str <sub>subscript</sub> str <sup>superscript</sup>

    assert text_formatting.convert('str **bold** str _italic_ str ~~strikethrough~~ str <sub>subscript</sub> str <sup>superscript</sup>') == 'str <strong>bold</strong> str <em>italic</em> str <del>strikethrough</del> str <sub>subscript</sub> str <sup>superscript</sup>'

