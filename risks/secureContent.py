from controllers import Prio, Colors
from .risk import Risk
class SecureContent(Risk):
    def __init__(self, loc, excerpt):
        Risk.__init__(self,
        'Insecure Protocol',
        'Any resources not included with your application should be loaded using a secure protocol like HTTPS. In other words, do not use insecure protocols like HTTP. Similarly, we recommend the use of WSS over WS, FTPS over FTP, and so on.',
        loc,
        excerpt,
        Prio.PRETTY_BAD,
        'https://www.electronjs.org/docs/tutorial/security#1-only-load-secure-content')

