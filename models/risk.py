from controllers import Prio, Colors, fetchExcerpt
from rich.text import Text
from rich.rule import Rule
from rich.table import Column, Table
from rich .panel import Panel

# Intended to be abstract
class Risk ():
    def __init__ (self, name, desc, loc, prio, link=None):
        self.name = name
        self.desc = desc
        self.loc = loc
        self.prio = prio
        self.link = link
        self.path = None

    def setPath (self, path):
        self.path = path

    def toString (self, verbose:bool = False, graphical: bool = False) -> list:
        return [self.nameToString(graphical), self.description(verbose, graphical), self.locationString(graphical), self.excerptView(graphical), '\n\n']

    def excerptView (self, graphical: bool):
        excerpt = fetchExcerpt(self.path, self.loc)
        if not graphical: return excerpt
        return Panel(excerpt)

    def locationString (self, graphical: bool):
        if not graphical: return self.Text
        return Text(self.path, style='italic bold blue')

    def description (self, verbose:bool, graphical: bool):
        if not graphical:
            if verbose: return self.desc + '\n' + self.link
            else: return self.link

        string = None
        if verbose:
            string = self.desc + ' [bold blue]' + self.link+ '[/bold blue]'
        else:
            string = self.link
        return Panel(string, style='black bold')

    def nameToString (self, graphical: bool):
        if not graphical: return self.name
        styleStr = None
        if self.prio == Prio.VERY_BAD: styleStr = "bold red"
        if self.prio == Prio.PRETTY_BAD: styleStr = "bold yellow"
        if self.prio == Prio.NOT_GOOD: styleStr = "bold blue"
        
        return Rule(Text(self.name, style=styleStr, justify='center'), style='bold grey')

        
