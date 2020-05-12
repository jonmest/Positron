from ..prio import Prio
from ..risk import Risk

class Remote(Risk):
    def __init__(self, loc, excerpt=True):
        Risk.__init__(self,
        'Disable or filter the remote module',
        'The remote module provides a way for the renderer processes to access APIs normally only available in the main process. Using it, a renderer can invoke methods of a main process object without explicitly sending inter-process messages. If your desktop application does not run untrusted content, this can be a useful way to have your renderer processes access and work with modules that are only available to the main process, such as GUI-related modules (dialogs, menus, etc.). If you cannot disable the remote module, you should filter the globals, Node, and Electron modules (so-called built-ins) accessible via remote that your application does not require. This can be done by blocking certain modules entirely and by replacing others with proxies that expose only the functionality that your app needs.',
        loc,
        Prio.VERY_BAD,
        'https://www.electronjs.org/docs/tutorial/security#15-disable-the-remote-module',
        excerpt=excerpt)

