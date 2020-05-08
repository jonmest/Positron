from collections.abc import Iterable   # drop `.abc` with Python 2.7 or lower
import esprima
import inspect
import re
globalPositives = []
globalNegatives = []
program = """
const URL = require('url').URL

app.on('web-contents-created', (event, contents) => {
  contents.on('will-s', (event, navigationUrl) => {
    const parsedUrl = new URL(navigationUrl)

    contents.on('will-navigate', (event, navigationUrl) => {
    const parsedUrl = new URL(navigationUrl)

    if (parsedUrl.origin !== 'https://example.com') {
      event.preventDefault()
    }
})
  })
})
"""

#^^^ 
# In will-navigate listener, should have an event.preventDefault
def isNavigationDisabled (node):
    if (node.type == 'ExpressionStatement'):
        if hasattr(node.expression.callee, 'property'):
            if node.expression.callee.property.name == "on":
                for x in node.expression.arguments:
                    if x.type == "Literal" and x.value == "will-navigate":
                        return ([], ["will-navigate"])

    return ([], [])

def isThereListenerForWebView (node):
    if (node.type == 'ExpressionStatement'):
        if hasattr(node.expression.callee, 'property'):
            if node.expression.callee.property.name == "on":
                for x in node.expression.arguments:
                    if x.type == "Literal" and x.value == "will-attach-webview":
                        return ([], ["will-attach-webview"])

    return ([], [])

def isBlinkFeaturesTrue (node):
    if (node.type == 'ObjectExpression'):
        for x in node.properties:
            if x.key.name == "enableBlinkFeatures":
                return (['enableBlinkFeatures'], [])
    return ([], [])

def isExperimentalFeaturesTrue (node):
    if (node.type == 'ObjectExpression'):
        for x in node.properties:
            if x.key.name == "experimentalFeatures":
                if x.value.value == True:
                    return (['experimentalFeatures'], [])
    return ([], [])

def isAllowRunningInsecureContentTrue (node):
    if (node.type == 'ObjectExpression'):
        for x in node.properties:
            if x.key.name == "allowRunningInsecureContent":
                if x.value.value == True:
                    return (['allowRunningInsecureContent'], [])
    return ([], [])

def isWebSecurityDisabled (node):
    if (node.type == 'ObjectExpression'):
        for x in node.properties:
            if x.key.name == "webSecurity":
                if x.value.value == False:
                    return (['isWebSecurityDisabled'], [])
    return ([], [])

def isSet (node):
    if (node.type == 'CallExpression'):
        if node.callee.name == "setPermissionRequestHandler":
            return ([], ['setPermissionRequestHandler'])
        elif getattr(node.callee, 'property'):
            if node.callee.property.name  == "setPermissionRequestHandler":
                return ([], ['setPermissionRequestHandler'])
    return ([], [])

def isContextIsolationTrue (node):
    if (node.type == 'ObjectExpression'):
        for x in node.properties:
            if x.key.name == "contextIsolation":
                if x.value.value == True:
                    return ([], ['contextIsolation'])
    return ([], [])

def isNodeIntegrationTrue (node):
    if (node.type == 'ObjectExpression'):
        for x in node.properties:
            if x.key.name == "nodeIntegration":
                if x.value.value == True:
                    return (['Node integration.'], [])
            if x.key.name == 'nodeIntegrationInWorker':
                if x.value.value == True:
                    return (['Node integrationWorker.'], [])
    return ([], [])

def isBadURL (node):
    if (node.type == "Literal"):
        if (
            "http:" in node.value.lower() or
            "ws:" in node.value.lower() or
            "ftp:" in node.value.lower()
        ): return (['Insecure protocol.'], [])
    return ([], [])

patterns = [isNavigationDisabled]

def checkPatterns (node, patterns):
    for pattern in patterns:
        results: tuple = pattern(node)
        globalPositives.extend(results[0])
        globalNegatives.extend(results[1])

def traverse (node, meta):
    checkPatterns(node, patterns)

e = esprima.parseScript(program, loc=True, delegate=traverse)

print(globalPositives)
print(globalNegatives)