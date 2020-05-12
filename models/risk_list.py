from .prio import Prio
from .risk import Risk
from lexer.pattern_store import PatternStore
from .positive_expected import expected

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
        self.positiveList = [ *self.positiveList, *toMerge.positiveList]
        self.negativeList = [ *self.negativeList,  *toMerge.negativeList]

    def negativeToString (self, verbose: bool = False, graphical: bool = False):
        n = []
        for item in self.negativeList:
            n.append(item.toString(verbose, graphical))
        print(n)
        return n

    def positiveToString (self, verbose: bool = False, graphical: bool = False):
        p = []
        for item in expected:
            if not item in self.positiveList:
                p.append(item.toString(verbose, graphical))
        return p