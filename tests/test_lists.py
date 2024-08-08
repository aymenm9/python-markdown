from pytest import *
import sys
import os
# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from markdown import order_list, unordered_list

def test_order_lists():
 
    assert order_list.convert('') == ''
    # test order lists
    # markdown: 1. list
    # html: <ol><li>list</li></ol>
    assert order_list.convert(('1. list',)) == '<ol><li>list</li></ol>'

    # test order lists
    # markdown: 1. list1
    #           2. list2
    #           ['1. list1', '2. list2']
    # html: <ol><li>list1</li><li>list2</li></ol>
    assert order_list.convert(('1. list1', '2. list2')) == '<ol><li>list1</li><li>list2</li></ol>'

def test_unordered_lists():

    assert unordered_list.convert('') == ''
    # test unordered lists
    # markdown: - list
    # html: <ul><li>list</li></ul>
    assert unordered_list.convert(('- list',)) == '<ul><li>list</li></ul>'

    # test unordered lists
    # markdown: - list1
    #           * list2
    #           ['- list1', '* list2']
    # html: <ul><li>list1</li><li>list2</li></ul>
    assert unordered_list.convert(('- list1', '* list2')) == '<ul><li>list1</li><li>list2</li></ul>'


