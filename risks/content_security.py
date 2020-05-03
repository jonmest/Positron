from prio import Prio
from colors import Colors
from .risk import Risk

class Content_Security(Risk):
    def __init__(self, loc, excerpt):
        Risk.__init__(self,
        'Define a Content Security Policy',
        'A Content Security Policy (CSP) is an additional layer of protection against cross-site-scripting attacks and data injection attacks. We recommend that they be enabled by any website you load inside Electron.',
        loc,
        excerpt,
        Prio.PRETTY_BAD,
        'https://www.electronjs.org/docs/tutorial/security#6-define-a-content-security-policy')

