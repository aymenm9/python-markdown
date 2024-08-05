import os


files_names = [
    #first levle
    'test_headers.py',
    'test_blockquotes.py',
    'test_lists.py',
    'test_tables.py',
    'test_code_blocks.py',
    'test_html_elements.py',
    'test_html_blocks.py',
    'test_paragraphs.py',

    #second level
    'test_text_formatting.py',
    'test_links.py',
    'test_images.py',
    'test_line_breaks.py',
    'test_list_items.py',

    ]


def main():
    for file in files_names:
        if not os.path.isfile(file):
            with open(file, 'w') as f:
                f.write('from pytest import *')
                f.write('\n')
                f.write(f'def {file[:-3]}():')
                f.write('\tpass')

if __name__ == '__main__':
    main()