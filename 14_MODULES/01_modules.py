'''
There are two types of modules:
    - Internal
        - These are modules such as math, date, io
    - External
        - These are user made modules can be our own or installed through a utility called pip
'''
# Internal
import math
import os

print(math.sqrt(16))
print(os.environ)

# External
import myModule
print(myModule.hello())

# External installed with pip
"""
In the terminal run the command pip install <moduleName>
"""
import requests
r = requests.get("http://google.com")
print(r.text)