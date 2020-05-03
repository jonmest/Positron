from prio import Prio
from colors import Colors
from .risk import Risk

class Open_External(Risk):
    def __init__(self, loc, excerpt):
        Risk.__init__(self,
        'Do not use openExternal with untrusted content',
        'Shell\'s openExternal allows opening a given protocol URI with the desktop\'s native utilities. On macOS, for instance, this function is similar to the open terminal command utility and will open the specific application based on the URI and filetype association.',
        loc,
        excerpt,
        Prio.VERY_BAD,
        'https://www.electronjs.org/docs/tutorial/security#14-do-not-use-openexternal-with-untrusted-content')

