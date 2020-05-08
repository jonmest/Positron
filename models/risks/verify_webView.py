from controllers import Prio, Colors
from ..risk import Risk

class Verify_WebView(Risk):
    def __init__(self, loc):
        Risk.__init__(self,
        'Verify WebView Options Before Creation',
        'It is a good idea to control the creation of new <webview> tags from the main process and to verify that their webPreferences do not disable security features.',
        loc,
        Prio.PRETTY_BAD,
        'https://www.electronjs.org/docs/tutorial/security#10-do-not-use-allowpopups')

