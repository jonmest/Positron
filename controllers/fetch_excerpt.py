from .colors import Colors
from rich.console import Console
from rich.syntax import Syntax
console = Console()

def fetchExcerpt (path: str, line_count: int) -> Syntax:
    string = ''
    try:
        fp = open(path, 'r')
        line = fp.readline()
        count = 1
        
        while line:
            if (count >= line_count - 2 and count <= line_count + 2):
                string += line
            line = fp.readline()
            count += 1
    finally:
        fp.close()
    return Syntax(string, 'javascript', theme="monokai", line_numbers=True, start_line=line_count-2)