import re
'''
|   |-- Text styling
|   |   |-- Bold
|   |   |-- Italic
|   |   |-- Strikethrough
|   |   |-- Bold and nested italic
|   |   |-- All bold and italic
|   |   |-- Subscript
|   |   |-- Superscript
'''
class text_formatting_class:
    def __init__(self):
        pass
    
    def gen_text_formatting(self, match):
        

        return match.group(1)
    
    def convert(self, text: str) -> str:
        '''
        text formatting

        Parameters
        ----------
        text : str
            The text to format

        Returns
        -------
        str
            The formatted text
        
        
        '''

        if len(text) == 0:
            return ""

        # format all bold and italic befor bold cause bold [**(*str)**]* & same for other formats order is important
        bold_and_italic = re.findall(r'(\*\*\*)(.*?)(\*\*\*)', text)
        for b in bold_and_italic:
            text = text.replace(''.join(b), self.all_bold_and_italic(b[1]))

        # format bold
        bold = re.findall(r'(\*\*|__)(.*?)(\*\*|__)', text)
        for b in bold:
            text = text.replace(''.join(b), self.bold(b[1]))
        # format italic
        italic = re.findall(r'(_|\*)(.*?)(_|\*)', text)
        for i in italic:
            text = text.replace(''.join(i), self.italic(i[1]))
        
        # format strikethrough
        strikethrough = re.findall(r'(~~)(.*?)(~~)', text)
        for s in strikethrough:
            text = text.replace(''.join(s), self.strikethrough(s[1]))

        # format bold and italic will be converted automatically in the bold and italic 
        '''
        # format subscript
        sub = re.findall(r'(~)(.*?)(~)', text)
        
        for s in sub:
            text = text.replace(''.join(s), self.subscript(s[1]))

        # format superscript
        sup = re.findall(r'(\^)(.*?)(\^)', text)

        for s in sup:
            text = text.replace(''.join(s), self.superscript(s[1]))
        '''
        return text


    def bold(self, text):
       return f'<strong>{text}</strong>'

    def italic(self, text):
        return f'<em>{text}</em>'

    def strikethrough(self, text):
        return f'<del>{text}</del>'

    def bold_and_italic(self, text):
        # call bold and italic from convert function
        pass

    def all_bold_and_italic(self, text):
        return self.bold(self.italic(text))

    def subscript(self, text):
        return f'<sub>{text}</sub>'

    def superscript(self, text):
        return f'<sup>{text}</sup>'



# singleton only on obj text_formatting

text_formatting = text_formatting_class()