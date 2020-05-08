class PatternStore:
    def __init__(self):
        self.positives = []
        self.negatives = []

    def addPositive (self, positive):
        self.positives.append(positive)
    
    def addNegative (self, negative):
        self.negatives.append(negative)
