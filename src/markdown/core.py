import os


def convert(markdown):
    """
    Convert Markdown to HTML

    Parameters
    ----------
    markdown : str
        The Markdown text to convert

    Returns
    -------
    str
        The converted HTML text
    """

    if not os.path.isfile(markdown):
        raise FileNotFoundError

    with open(markdown, 'r') as f:
        for line in f:
            print(line)

        

    return markdown

