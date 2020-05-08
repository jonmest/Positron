from .colors import Colors
from rich.console import Console
from rich.syntax import Syntax
console = Console()

def fetchExcerpt (path: str, loc: dict) -> Syntax:
    string = ''
    start = loc.start.line
    end = loc.end.line

    try:
        fp = open(path, 'r')
        line = fp.readline()
        count = 1
        
        while line:
            if (start <= count <= end):
                string += line
            line = fp.readline()
            count += 1
        fp.close()
    except:
        print("Something messed up.")
    return Syntax(string, 'javascript', theme="monokai", line_numbers=True, start_line=start)