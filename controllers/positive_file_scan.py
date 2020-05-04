from models import Risk_List
from .analyze_line import analyze_line 

# Find patterns that should NOT occur, but do.
def positive_file_scan (list_of_files: list) -> Risk_List:
    risks: Risk_List = Risk_List()
    for f in list_of_files:
        risks.merge(private_positive_file_scan(f))
    return risks

def private_positive_file_scan (path: str) -> Risk_List:
    risks = Risk_List()
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