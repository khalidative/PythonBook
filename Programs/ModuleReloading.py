#======================================================
# "ModuleReloading.py" 
# This program shows the python interpreters behaviour
# when there are multiple imports on a module.
#======================================================
import imp

import Example
imp.reload(Example)
imp.reload(Example)