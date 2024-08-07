import re


class links_class:

    def __init__(self):
        pass
    def convert(self, line):

        '''
        Convert line that contains links

        Parameters
        ----------
        line : str
            The line to convert

        Returns
        -------
        str
            The converted line in HTML
        '''

        if len(line) == 0:
            return ""
        # *******************0****1***2****3***4***5
        like = re.findall(r'(\[)(.*?)(\])(\()(.*?)(\))' ,line)

        for l in like:
            line = line.replace(''.join(l), self.link(l[1],l[4]))

        return line

    def link(self, text, link):
        return f'<a href="{link}">{text}</a>'

links = links_class()