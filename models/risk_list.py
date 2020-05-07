from controllers import Prio, Colors
from .risk import Risk

class Risk_List:
    def __init__ (self):
        self.list: list = []
    
    def push (self, toPush: Risk):
        self.list.append(toPush)

    def merge (self, toMerge):
        self.list = self.list + toMerge.list

    def toString (self, verbose: bool = False, graphical: bool = False):
        string = []
        for item in self.list:
            string.append(item.toString(verbose, graphical))
        return string
