
class headers_class:
    def __init__(self):
        pass

    def h(self, level, text):
        return "<h" + str(level) + ">" + text + "</h" + str(level) + ">"

    def convert(self, line):

        '''
        Convert headers

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

        level = 0
        text = ""

        # Find the level of the header and the text

        if line[0] == '#':
            level = 1
            text = line[2:].strip()
        elif line[0:2] == '##':
            level = 2
            text = line[3:].strip()
        elif line[0:3] == '###':
            level = 3
            text = line[4:].strip()
        elif line[0:4] == '####':
            level = 4
            text = line[5:].strip()
        elif line[0:5] == '#####':
            level = 5
            text = line[6:].strip()
        elif line[0:6] == '######':
            level = 6
            text = line[7:].strip()
        else:
            return line

        return self.h(level, text)
    
headers = headers_class()