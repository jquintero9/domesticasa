from .base import *

try:
    from .local import *
    production = False
except Exception:
    production = True

if production:
    from .production import *