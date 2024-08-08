import os
from convert import convert

def convert_to_html(markdown):
    """
    Convert Markdown to HTML

    Parameters
    ----------
    markdown : str
        The Markdown file path to convert

    Returns
    -------
    str
        The converted HTML text
    """

    if not os.path.isfile(markdown):
        raise FileNotFoundError

    html = convert(markdown)

    return html

def main():
    markdown = "test.md"
    html = convert_to_html(markdown)
    print(html)

if __name__ == "__main__":
    main()
