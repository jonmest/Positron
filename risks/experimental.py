from controllers import Prio, Colors
from .risk import Risk

class Experimental(Risk):
    def __init__(self, loc, excerpt):
        Risk.__init__(self,
        'Do Not Enable Experimental Features',
        'Experimental features are, as the name suggests, experimental and have not been enabled for all Chromium users. Furthermore, their impact on Electron as a whole has likely not been tested. Legitimate use cases exist, but unless you know what you are doing, you should not enable this property.',
        loc,
        excerpt,
        Prio.NOT_GOOD,
        'https://www.electronjs.org/docs/tutorial/security#8-do-not-enable-experimental-features')

