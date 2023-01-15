

import os,sys

sys.path.append("..")

from tools.iPrint import *
from misc.Color import Colors

class Shell:
    def __init__(self) -> None:
        self.runShell()

    def runShell(self):
        while True:
            try:
                command = input(Colors.RED + "IShell ~$shell> " + Colors.END)
                if command in ["q", "quit", "exit", "exit()"]:
                    return 0
                else:
                    os.system(command)
            except KeyboardInterrupt:
                return 0
            except Exception as e:
                print(Colors.RED + "[!]" + Colors.END + "Error: " + e)

Shell()

