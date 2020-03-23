import urllib.request
import sys
import types

def load_module(url):
    u = urllib.request.urlopen(url)
    source = u.read().decode('utf-8')
    # mod = sys.modules.setdefault(url, imp.new_module(url))
    mod = sys.modules.setdefault(url, types.ModuleType(url))
    code = compile(source, url, 'exec')
    mod.__file__ = url
    mod.__package__ = ''
    exec(code, mod.__dict__)
    return mod
