from colors import Colors
from prio import Prio

class Risk ():
    def __init__ (self, name, desc, loc, excerpt, prio, link=None):
        self.name = name
        self.desc = desc
        self.loc = loc
        self.excerpt = excerpt
        self.prio = prio
        self.link = link

    def toString (self):
        return self.nameToString() + ' found at ' + self.loc + ':\n ' + self.excerpt + '\nn' + self.desc + ' [' + self.linkToString() + ']'

    def linkToString (self):
        if self.link == None:
            return ''
        else:
            return self.link

    def nameToString (self):
        color = ''
        
        if self.prio == Prio.VERY_BAD:
            color = Colors.FAIL
        if self.prio == Prio.PRETTY_BAD:
            color = Colors.WARNING
        if self.prio == Prio.NOT_GOOD:
            color = Colors.OKBLUE
        
        return color + self.name + Colors.ENDC
