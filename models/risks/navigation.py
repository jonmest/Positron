from controllers import Prio, Colors
from ..risk import Risk

class Navigation(Risk):
    def __init__(self, loc):
        Risk.__init__(self,
        'Disable or limit navigation',
        'If your app has no need to navigate or only needs to navigate to known pages, it is a good idea to limit navigation outright to that known scope, disallowing any other kinds of navigation.',
        loc,
        Prio.PRETTY_BAD,
        'https://www.electronjs.org/docs/tutorial/security#12-disable-or-limit-navigation')

