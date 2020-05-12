from ..prio import Prio
from ..risk import Risk

class NodeIntegration(Risk):
    def __init__(self, loc, excerpt=True):
        Risk.__init__(self,
        'Node Integration',
        'It is paramount that you do not enable Node.js integration in any renderer (BrowserWindow, BrowserView, or <webview>) that loads remote content. The goal is to limit the powers you grant to remote content, thus making it dramatically more difficult for an attacker to harm your users should they gain the ability to execute JavaScript on your website.',
        loc,
        Prio.PRETTY_BAD,
        'https://www.electronjs.org/docs/tutorial/security#1-only-load-secure-content',
        excerpt=excerpt)

