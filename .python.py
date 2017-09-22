import os
import datetime
import sys

try:
    import readline
except ImportError:
    print("Module readline not available")
else:
    import rlcompleter
    readline.parse_and_bind("tab: complete")

name = os.getlogin()

if os.getcwd()=="/home/kukushka":
     print "\nHello", name, "and wecome to Python"

try:
    from app import models
    from django.conf import settings
except:
    print("\nCould not find your Django modules.\n")
else:
   print("\nSuccessfully imported your Djanjo modules.\n")

from pprint import pprint
try:
    from tabulate import tabulate
except ImportError:
    pass

# Command history
import atexit

historyPath = os.path.expanduser("~/.python_history")
def save_history(historyPath=historyPath):
    readline.write_history_file(historyPath)

if os.path.exists(historyPath):
    readline.read_history_file(historyPath)

atexit.register(save_history)

