from controllers import Prio, Colors
from .risk import Risk

class Disable_New_Windows(Risk):
    def __init__(self, loc, excerpt):
        Risk.__init__(self,
        'Disable or limit creation of new windows',
        'If you have a known set of windows, it\'s a good idea to limit the creation of additional windows in your app.',
        loc,
        excerpt,
        Prio.PRETTY_BAD,
        'https://www.electronjs.org/docs/tutorial/security#13-disable-or-limit-creation-of-new-windows')

