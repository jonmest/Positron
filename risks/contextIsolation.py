from prio import Prio
from colors import Colors
from .risk import Risk

class ContextIsolation(Risk):
    def __init__(self, loc, excerpt):
        Risk.__init__(self,
        'Context isolation',
        'Context isolation is an Electron feature that allows developers to run code in preload scripts and in Electron APIs in a dedicated JavaScript context. In practice, that means that global objects like Array.prototype.push or JSON.parse cannot be modified by scripts running in the renderer process.',
        loc,
        excerpt,
        Prio.PRETTY_BAD,
        'https://www.electronjs.org/docs/tutorial/security#1-only-load-secure-content')

