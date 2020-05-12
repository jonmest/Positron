from ..prio import Prio
from ..risk import Risk

class Blink(Risk):
    def __init__(self, loc, excerpt=True):
        Risk.__init__(self,
        'Do Not Use enableBlinkFeatures',
        'As a developer, you should know exactly why you need to enable a feature, what the ramifications are, and how it impacts the security of your application. Under no circumstances should you enable features speculatively.',
        loc,
        Prio.NOT_GOOD,
        'https://www.electronjs.org/docs/tutorial/security#9-do-not-use-enableblinkfeatures',
        excerpt=excerpt)

