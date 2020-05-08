from controllers import Prio, Colors
from .risk import Risk
from lexer.pattern_store import PatternStore

class Risk_List:
    def __init__ (self):
        self.positiveList: list = []
        self.negativeList: list = []
    
    def load (self, patternStore, path):
        for i in patternStore.negatives:
            i.setPath(path)
        for i in patternStore.positives:
            i.setPath(path)
        
        self.negativeList.extend(patternStore.negatives)
        self.positiveList.extend(patternStore.positives)

    def merge (self, toMerge):
        self.positiveList = self.positiveList + toMerge.positiveList
        self.negativeList = self.negativeList + toMerge.negativeList

    def toString (self, verbose: bool = False, graphical: bool = False):
        l = []
        for item in self.negativeList:
            l.append(item.toString(verbose, graphical))
        return l
