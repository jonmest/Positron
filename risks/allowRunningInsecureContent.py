from controllers import Prio, Colors
from .risk import Risk

class AllowRunningInsecureContent(Risk):
    def __init__(self, loc, excerpt):
        Risk.__init__(self,
        'Do Not Set allowRunningInsecureContent to true',
        'By default, Electron will not allow websites loaded over HTTPS to load and execute scripts, CSS, or plugins from insecure sources (HTTP). Setting the property allowRunningInsecureContent to true disables that protection. Loading the initial HTML of a website over HTTPS and attempting to load subsequent resources via HTTP is also known as "mixed content".',
        loc,
        excerpt,
        Prio.PRETTY_BAD,
        'https://www.electronjs.org/docs/tutorial/security#7-do-not-set-allowrunninginsecurecontent-to-true')

