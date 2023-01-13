
import os
import sys

sys.path.append("..")

from tools.SelfCheck import SelfCheck
from tools.iPrint import *


unready = SelfCheck.LibCheckNative()

if len(unready) == 0: 
    iPrintLog("Nothing to download", "Downlib", "Main", "warning")
    exit(0)

iPrintLog("Ready to download", "Downlib", "Main", "info")
for lib in unready:
    os.system("pip install "+lib)
    iPrintLog(lib + " download!", "Downlib", "Main", "success")

iPrintLog("Download Finish!", "Downlib", "Main", "success")
