from models import Risk_List
from .analyze_line import analyze_line 
from lexer.pattern_store import PatternStore
from lexer.analyze import analyze

def fileScan (path: str):
    risks = Risk_List()
    patternStore = PatternStore()
    try:
        fp = open(path, 'r')
        code = fp.read()
        analyze(code, patternStore)
    except:
        print("Something went wrong when scanning " + path + 
        "\nEither there is a syntax error, invalid ECMAScript, or you mix JSX in normal JS-files.\n")
    finally:
        fp.close()
    risks.load(patternStore, path)
    return risks