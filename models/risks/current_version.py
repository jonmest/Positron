from controllers import Prio, Colors
from ..risk import Risk

class Current_Version(Risk):
    def __init__(self, loc):
        Risk.__init__(self,
        'Use a current version of Electron',
        'You should strive for always using the latest available version of Electron. Whenever a new major version is released, you should attempt to update your app as quickly as possible.',
        loc,
        Prio.PRETTY_BAD,
        'https://www.electronjs.org/docs/tutorial/security#17-use-a-current-version-of-electron')

