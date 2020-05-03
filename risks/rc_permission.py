from prio import Prio
from colors import Colors
from .risk import Risk

class RC_Permission(Risk):
    def __init__(self, loc, excerpt):
        Risk.__init__(self,
        'Handle Session Permission Requests From Remote Content',
        'By default, Electron will automatically approve all permission requests unless the developer has manually configured a custom handler. While a solid default, security-conscious developers might want to assume the very opposite.',
        loc,
        excerpt,
        Prio.NOT_GOOD,
        'https://www.electronjs.org/docs/tutorial/security#4-handle-session-permission-requests-from-remote-content')

