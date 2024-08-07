import re
from typing import Generator
from .html_elements import *
from .html_elements.lists import lists_class, order_list_class, unordered_list_class


def generate_segments(file: str) -> Generator[dict, None, None]:
    """
    Generate segments of Markdown

    now it only supports headers, lists

    Parameters
    ----------
    text : str
        The Markdown text to convert

    Returns
    -------
    generator
        dict
            segments of Markdown

    Examples
    --------
        {'header': '# header 1'}
        
    """

    buffer = [list(),'']
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if buffer[1] == 'ul':
                if re.match(r'^[\*\+-] *', line):
                    buffer[0].append(line)
                else:
                    lins = buffer[0]
                    buffer[0] = list()
                    buffer[1] = ''
                    yield (unordered_list , lins)

            elif buffer[1] == 'ol':
                if re.match(r'^[0-9]+\. *', line):
                    buffer[0].append(line)
                else:
                    lins = buffer[0]
                    buffer[0] = list()
                    buffer[1] = ''
                    yield (order_list , lins)

            if buffer[1] == '':
                if line.startswith('#'):
                    yield ( headers , line)
                elif re.match(r'^[\*\+-] *', line):
                    buffer[1] = 'ul'
                    buffer[0].append(line)
                elif re.match(r'^[0-9]+\. *', line):
                    buffer[1] = 'ol'
                    buffer[0].append(line)
                else:
                    yield (paragraph , line.strip())
        if buffer[1]:
            yield (order_list if buffer[1] == 'ol' else unordered_list, buffer[0])
            
def convert(file) -> str:
    html = ''

    for converter , segment in generate_segments(file):
        if isinstance(converter,(order_list_class,unordered_list_class)):
            for i in range(len(segment)):
                segment[i] = text_formatting.convert(segment[i])
                segment[i] = links.convert(segment[i])
        else:
            segment = text_formatting.convert(segment)
            segment = links.convert(segment)
        html += converter.convert(segment)
    return html