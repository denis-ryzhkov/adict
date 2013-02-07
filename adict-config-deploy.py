'''
HINT:

If you have single config based on adict,
and this config is used by both project and deploy script that installs virtualenv/pip/adict,
then you may sacrifice attr access in deploy script only, put preserve it in the project body
with the next workaround in deploy script:
'''

import sys
try:
    from adict import adict
except ImportError:
    adict = dict
    sys.modules['adict'] = sys.modules[__name__]
