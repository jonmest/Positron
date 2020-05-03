import os
import re
import sys
from analyze_file import analyze_file

path = sys.argv[1]

files = []

for r, d, f in os.walk(path):
    for file in f:
        if '.js' in file:
            files.append(os.path.join(r, file))

for f in files:
    risks = analyze_file(f)
    print(risks.toString())
