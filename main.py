import os
import re
import sys
from analyze_file import analyze_file

path = sys.argv[1]

blacklist = ('json', 'package', 'package-lock.json', 'node_modules', 'build', 'dist')
demandList = ('.js',)
files = []

def cleaner (items: list, blacklist: tuple = (), demandList: tuple = ()):
    clean = items.copy()
    for b in blacklist:
        clean = list(filter(lambda x: not b in x, clean))

    for d in demandList:
        clean = list(filter(lambda x: d in x, clean))

    return clean

for r, d, f in os.walk(path):
    [files.append(os.path.join(r, file)) for file in f]
list_of_files = cleaner(files, blacklist, demandList)

for f in list_of_files:
    risks = analyze_file(f)
    print(risks.toString())
