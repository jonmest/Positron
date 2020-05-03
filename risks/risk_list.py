from prio import Prio
from colors import Colors
from .risk import Risk

class Risk_List:
    def __init__ (self):
        self.list: list = []
    
    def push (self, toPush):
        self.list.append(toPush)

    def toString (self):
        string = ''
        for item in self.list:
            string += '\n\n' + item.toString() + '\n'
        return string
