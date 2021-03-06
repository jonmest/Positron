from ..prio import Prio
from ..risk import Risk

class Allow_Popups(Risk):
    def __init__(self, loc, excerpt=True):
        Risk.__init__(self,
        'Do Not Use allowpopups',
        'If you do not need popups, you are better off not allowing the creation of new BrowserWindows by default. This follows the principle of minimally required access: Don\'t let a website create new popups unless you know it needs that feature.',
        loc,
        Prio.PRETTY_BAD,
        'https://www.electronjs.org/docs/tutorial/security#10-do-not-use-allowpopups',
        excerpt=excerpt)

