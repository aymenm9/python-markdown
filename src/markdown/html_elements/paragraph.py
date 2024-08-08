class paragraph_class:

    def __init__(self):
        pass

    def convert(self, text):
        if len(text) == 0:
            return ""
        return '<p>' + text + '</p>'

paragraph = paragraph_class()