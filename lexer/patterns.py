import models as r
# POSITIVE PATTERNS
# Should occur. Bad if they dont.

def isRemoteDisabled (node, patternStore):
    if (node.type == 'ObjectExpression'):
        for x in node.properties:
            if x.key.name == "enableRemoteModule":
                if x.value.value == False:
                    patternStore.addPositive(
                        r.Remote(node.loc)
                    )

# If openExternal with a variable as URL argument
# IE, it may come from user input.
def untrustedOpenExternal (node, patternStore):
    if (node.type == 'CallExpression'):
        if node.callee.name == "openExternal":
                if node.arguments[0].type == "Identifier":
                    patternStore.addPositive(
                        r.Open_External(node.loc)
                    )
        elif getattr(node.callee, 'property'):
            if node.callee.property.name  == "openExternal":
                if node.arguments[0].type == "Identifier":
                    patternStore.addPositive(
                        r.Open_External(node.loc)
                    )

def isThereListenerNewWindow (node, patternStore):
    if (node.type == 'ExpressionStatement'):
        if hasattr(node.expression.callee, 'property'):
            if getattr(node.expression.callee.property, 'name', False) == "on":
                for x in node.expression.arguments:
                    if x.type == "Literal" and x.value == "new-window":
                        patternStore.addPositive(
                            r.Disable_New_Windows(node.loc)
                        )

def isNavigationDisabled (node, patternStore):
    if (node.type == 'ExpressionStatement'):
        if hasattr(node.expression.callee, 'property'):
            if getattr(node.expression.callee.property, 'name', False) == "on":
                for x in node.expression.arguments:
                    if x.type == "Literal" and x.value == "will-navigate":
                        patternStore.addPositive(
                            r.Navigation(self.loc)
                        )

def isThereListenerForWebView (node, patternStore):
    if (node.type == 'ExpressionStatement'):
        if hasattr(node.expression.callee, 'property'):
            if getattr(node.expression.callee.property, 'name', False) == "on":
                for x in node.expression.arguments:
                    if x.type == "Literal" and x.value == "will-attach-webview":
                        patternStore.addPositive("will-attach-webview")

def isSetPermissionRequestHandler (node, patternStore):
    if (node.type == 'CallExpression'):
        if node.callee.name == "setPermissionRequestHandler":
            return ([], ['setPermissionRequestHandler'])
        elif getattr(node.callee, 'property'):
            if node.callee.property.name  == "setPermissionRequestHandler":
                patternStore.addPositive(
                    r.RC_Permission(node.loc)
                )

def isContextIsolationTrue (node, patternStore):
    if (node.type == 'ObjectExpression'):
        for x in node.properties:
            if x.key.name == "contextIsolation":
                if x.value.value == True:
                    patternStore.addPositive(
                        r.ContextIsolation(node.loc)
                    )

# NEGATIVE PATTERNS
# Should NOT occur. Bad if they do.

def isBlinkFeaturesTrue (node, patternStore):
    if (node.type == 'ObjectExpression'):
        for x in node.properties:
            if x.key.name == "enableBlinkFeatures":
                patternStore.addNegative(
                    r.Blink(node.loc)
                )

def isExperimentalFeaturesTrue (node, patternStore):
    if (node.type == 'ObjectExpression'):
        for x in node.properties:
            if x.key.name == "experimentalFeatures":
                if x.value.value == True:
                    patternStore.addNegative(
                        r.Experimental(node.loc)
                    )

def isAllowRunningInsecureContentTrue (node, patternStore):
    if (node.type == 'ObjectExpression'):
        for x in node.properties:
            if x.key.name == "allowRunningInsecureContent":
                if x.value.value == True:
                    patternStore.addNegative(
                        r.AllowRunningInsecureContent(node.loc)
                    )

def isWebSecurityDisabled (node, patternStore):
    if (node.type == 'ObjectExpression'):
        for x in node.properties:
            if x.key.name == "webSecurity":
                if x.value.value == False:
                    patternStore.addNegative(
                        r.Disabled_Websecurity(node.loc)
                    )

def isNodeIntegrationTrue (node, patternStore):
    if (node.type == 'ObjectExpression'):
        for x in node.properties:
            if x.key.name == "nodeIntegration":
                if x.value.value == True:
                    patternStore.addNegative(
                        r.NodeIntegration(node.loc)
                    )
            if x.key.name == 'nodeIntegrationInWorker':
                if x.value.value == True:
                    patternStore.addNegative(
                        r.NodeIntegration(node.loc)
                    )

def isBadURL (node, patternStore):
    if (node.type == "Literal"):
        if (
            "http:" in node.raw.lower() or
            "ws:" in node.raw.lower() or
            "ftp:" in node.raw.lower()
        ): patternStore.addNegative(r.SecureContent(node.loc))

PATTERNS = [untrustedOpenExternal, isRemoteDisabled, isBlinkFeaturesTrue, isThereListenerForWebView, isNavigationDisabled, isThereListenerNewWindow, isExperimentalFeaturesTrue, isBadURL, isNavigationDisabled, isNodeIntegrationTrue, isContextIsolationTrue, isSetPermissionRequestHandler, isWebSecurityDisabled, isAllowRunningInsecureContentTrue]