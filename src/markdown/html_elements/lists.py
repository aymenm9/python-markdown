from abc import ABC, abstractmethod
import re
class lists_class(ABC):

    def __init__(self):
        pass

    def convert(self, lines:list)->str:
        if len(lines) == 0:
            return ""
        out = ""
        # tempalte pattern 
        out += self.open()
        for line in lines:
            line = re.sub(r'([0-9]+\. *)|([\*\+-] *)','',line)
            out += '<li>' + line + '</li>'
        out += self.close(lines)

        return out

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self, lines):
        pass

class order_list_class(lists_class):

    def __init__(self):
        pass

    def open(self):
        return '<ol>'

    def close(self, lines):
        return '</ol>'


class unordered_list_class(lists_class):

    def __init__(self):
        pass

    def open(self):
        return '<ul>'

    def close(self, lines):
        return '</ul>'


order_list = order_list_class()
unordered_list = unordered_list_class()