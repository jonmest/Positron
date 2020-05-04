from .colors import Colors

def fetchExcerpt (path: str, line_count: int) -> str:
    string = ''
    try:
        fp = open(path, 'r')
        line = fp.readline()
        count = 1
        
        while line:
            if (count >= line_count - 1 and count <= line_count + 1):
                if (count == line_count):
                    string += '### ' + Colors.OKBLUE + line + Colors.ENDC
                else: string += '### ' + line
            line = fp.readline()
            count += 1
    finally:
        fp.close()
    return string