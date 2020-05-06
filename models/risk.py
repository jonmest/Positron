from controllers import Prio, Colors
from rich.text import Text
from rich.rule import Rule
from rich.table import Column, Table
from rich .panel import Panel
# Intended to be abstract
class Risk ():
    def __init__ (self, name, desc, loc, excerpt, prio, link=None):
        self.name = name
        self.desc = desc
        self.loc = loc
        self.excerpt = excerpt
        self.prio = prio
        self.link = link

    def toString (self, verbose:bool = False) -> list:
        return [self.nameToString(), self.description(verbose), self.locationString(), self.excerptView(), '\n\n']

    def excerptView (self):
        return Panel(self.excerpt)

    def linkToString (self):
        if self.link == None:
            return ''
        else:
            return self.link

    def locationString (self):
        n = Text(self.loc, style='italic bold blue')
        return n

    def description (self, verbose:bool = False):
        string = None
        if verbose:
            string = self.desc + ' [bold blue]' + self.link+ '[/bold blue]'
        else:
            string = self.link
            
        return Panel(string, style='black bold')



    def nameToString (self):
        styleStr = None
        if self.prio == Prio.VERY_BAD: styleStr = "bold red"
        if self.prio == Prio.PRETTY_BAD: styleStr = "bold yellow"
        if self.prio == Prio.NOT_GOOD: styleStr = "bold blue"
        
        return Rule(Text(self.name, style=styleStr, justify='center'), style='bold grey')

        
