from controllers import Prio, Colors
from .risk import Risk

class Risk_List:
    def __init__ (self):
        self.list: list = []
    
    def push (self, toPush: Risk):
        self.list.append(toPush)

    def merge (self, toMerge):
        self.list = self.list + toMerge.list

    def toString (self):
        string = ''
        for item in self.list:
            string += '\n' + item.toString() + '\n'
        return string