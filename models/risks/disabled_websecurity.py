from controllers import Prio, Colors
from ..risk import Risk

class Disabled_Websecurity(Risk):
    def __init__(self, loc):
        Risk.__init__(self,
        'Do Not Disable WebSecurity',
        'You may have already guessed that disabling the webSecurity property on a renderer process (BrowserWindow, BrowserView, or <webview>) disables crucial security features. Do not disable webSecurity in production applications.',
        loc,
        Prio.VERY_BAD,
        'https://www.electronjs.org/docs/tutorial/security#5-do-not-disable-websecurity')
