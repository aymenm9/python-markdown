import re
from typing import Generator
from html_elements import *

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

    with open(file, 'r') as f:
        for line in file:
            if line.startswith('#'):
                yield { headers : line}
            elif line.startswith('*'):
                pass
            




def convert_headers(text: str) -> str:
    """
    Convert segments of Markdown to HTML

    Parameters
    ----------
    text : str
        The Markdown text to convert

    Returns
    -------
    str
        The converted HTML text
    """


    return ""



