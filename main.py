import os
import re
import sys
from controllers import analyze_file

# Call this file with an argument pointing to the directory
# You want to analyze. For example: 
# `python3 main.py ~/electron-project/src`
path = sys.argv[1]

# Configure blacklist by adding patterns
# that shall not occur in ANY file or directory name
blacklist = ('package', '.json', 'node_modules', 'build', 'dist')

# Patterns that have to occur in files to analyze
# Don't see a need to change this, but the option exists
demandList = ('.js',)


files = []

# Clean a list according to specified black- and demand list
def cleaner (items: list, black_list: tuple = (), demand_list: tuple = ()) -> list:
    clean = items.copy()
    for b in black_list:
        clean = list(filter(lambda x: not b in x, clean))
    for d in demand_list:
        clean = list(filter(lambda x: d in x, clean))
    return clean

for r, d, f in os.walk(path):
    [files.append(os.path.join(r, file)) for file in f]

list_of_files = cleaner(files, blacklist, demandList)

for f in list_of_files:
    risks = analyze_file(f)
    print(risks.toString())
