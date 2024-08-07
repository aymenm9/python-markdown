import os


def convert_to_html(markdown):
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
        html = ""
        for line in f:
            html = html + line

        

    return html

def main():
    markdown = "test.md"
    html = convert_to_html(markdown)
    print(html)

if __name__ == "__main__":
    main()
