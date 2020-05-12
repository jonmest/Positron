import os
import re
import sys
from controllers import fileScan
from models import Risk_List
from rich.console import Console
from rich.text import Text

console = Console('standard')

# Call this file with an argument pointing to the directory
# You want to analyze. For example: 
# `python3 main.py ~/electron-project/src`
path = sys.argv[1]

setVerbose = False
setGraphical = True
for arg in sys.argv:
    if arg == '-v': setVerbose = True
    if arg == '-ng': setGraphical = False

# Configure blacklist by adding patterns
# that shall not occur in ANY file or directory name
blacklist = ('package', '.json', 'node_modules', 'build', 'dist')

# Patterns that have to occur in files to analyze
# Don't see a need to change this, but the option exists
demandList = ('.js',)

# Clean a list according to specified black- and demand list
def cleaner (items: list, black_list: tuple = (), demand_list: tuple = ()) -> list:
    clean = items.copy()
    for b in black_list:
        clean = list(filter(lambda x: not b in x, clean))
    for d in demand_list:
        clean = list(filter(lambda x: d in x, clean))
    return clean

files = []
for r, d, f in os.walk(path):
    [files.append(os.path.join(r, file)) for file in f]

list_of_files = cleaner(files, blacklist, demandList)
risks = Risk_List()

# Analyze a project in two waves
# 1. Negative scan
#   Find patterns that should NOT occur, but do.
#   This can be done line-by-line without storing
#   any kind of context, since one occurence is
#   enough to set of the alarm.
#
# 2. Positive scan
#   Find patterns that SHOULD occur, but don't.
#   When scanning like this, we need to keep
#   the complete project in mind, since an
#   absence of it in one file doesn't mean
#   it's absent from the whole project.
#
for file in list_of_files:
    risks.merge(fileScan(file))

for risk in risks.negativeToString(setVerbose, setGraphical):
    for item in risk:
        console.print(item)

for risk in risks.positiveToString(setVerbose, setGraphical):
    for item in risk:
        console.print(item)