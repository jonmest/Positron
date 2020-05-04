import risks as r
from .fetch_excerpt import fetchExcerpt

# Local class
class RiskPusher:
    def __init__(self, riskList, path, line, count):
        self.riskList = riskList
        self.path = path
        self.line = line
        self.count = count

    def push (self, risk):
        location = self.path + " Line " + str(self.count)
        self.riskList.push(risk(location, fetchExcerpt(self.path, self.count)))

class PatternMatcher:
    def __init__(self, string: str):
        self.string = string
    
    def matchPatterns (self, patterns: tuple, toLower: bool = False) -> bool:
        for p in patterns:
            cmpa = self.string
            if toLower: cmpa = self.string.lower()

            if type(p) is tuple:
                if p[0] in cmpa and p[1] in cmpa:
                    return True
            else:
                if p in cmpa:
                    return True
        return False



def pushRisk (riskList, risk, path, count):
    location = path + " Line " + str(count)
    riskList.push(risk(location))

def analyze_line (line: str, line_count: int, path: str, risks: r.Risk_List()):
    risk_pusher = RiskPusher(risks, path, line, line_count).push
    matcher = PatternMatcher(line).matchPatterns

    # Only load secure content
    if matcher(('http:', 'ws:', 'ftp:'), True):
        risk_pusher(r.SecureContent)

    # Do not enable Node.js Integration for Remote Content
    if matcher((
        ('nodeIntegrationInWorker', 'true'),
        ('nodeIntegration')
     )):
        risk_pusher(r.NodeIntegration)
    
    # Do Not Disable WebSecurity
    if matcher((
        ('webSecurity', 'false'),
        ('webSecurity', 'null'),
        ('webSecurity', '0'),
        'disablewebsecurity'
    )):
        risk_pusher(r.Disabled_Websecurity)

    # Do not allow all CSP
    if matcher((
        ('Content-Security-Policy', '*'),
    )):
        risk_pusher(r.Content_Security)
    
    # Do Not Set allowRunningInsecureContent to true
    if matcher((
        ('allowRunningInsecureContent', 'true'),
    )):
        risk_pusher(r.AllowRunningInsecureContent)

    # Do Not Enable Experimental Features
    if matcher((
        ('experimentalFeatures', 'true'),
    )):
        risk_pusher(r.Experimental)

    # Do Not Use enableBlinkFeatures
    if matcher(('enableBlinkFeatures',)):
        risk_pusher(r.Blink)

    # Do Not Use allowpopups
    if matcher(('allowpopups',)):
        risk_pusher(r.Allow_Popups)

    # Do not use openExternal with untrusted content
    if matcher(('openExternal',)):
        risk_pusher(r.Open_External)