import esprima
from .patterns import PATTERNS
from .pattern_store import PatternStore

def analyze (code: str, patternStore: PatternStore):
    def checkPatterns (node, patterns):
        for pattern in PATTERNS:
            pattern(node, patternStore)

    def traverse (node, meta):
        checkPatterns(node, PATTERNS)
    
    try:
        esprima.parseScript(code, loc=True, delegate=traverse, tolerant=True)
    except:
        esprima.parseScript(code, loc=True,
        delegate=traverse, tolerant=True, jsx=True)
