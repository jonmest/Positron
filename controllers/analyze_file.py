import risks as r
from .analyze_line import analyze_line 

def analyze_file (path: str) -> r.Risk_List:
    risks = r.Risk_List()
    try:
        fp = open(path, 'r')
        line = fp.readline()
        count = 1

        while line:
            analyze_line(line, count, path, risks)
            line = fp.readline()
            count += 1
    finally:
        fp.close()
    return risks