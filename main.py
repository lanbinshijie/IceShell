#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : Lanbin
# @Software: Vscode
# @Time    : 2023-1-13 18:49

import os, sys
from misc.Color import Colors
from misc.Logo import Logo
from tools.SelfCheck import SelfCheck
from misc.Info import ProgramInfo
from misc.Error import Error

def ExecuteModel(args, moduleName):
    if not SelfCheck.CheckModel(moduleName): return
    os.chdir(r"./models")
    if not os.path.exists(f"{moduleName}.py"):
        os.chdir(rf"./{moduleName}")
        command = sys.executable + f" ./main.py " + args
    else:
        command = sys.executable + f" ./{moduleName}.py " + args
    os.system(command)
    os.chdir(r"..")

def IceShell():
    extra = ""
    commandN = input(Colors.RED + extra + "IShell> " + Colors.END)
    command = commandN.split(" ")
    if command[0] in ProgramInfo.registered_modules or "*" in ProgramInfo.registered_modules:
        ExecuteModel(" ".join(command[1:]), command[0])
    elif command[0] == "q":
        print("Bye~")
        exit(0)
    else:
        Error.printError(10000)

if __name__ == "__main__":
    # 程序从这里开始
    SelfCheck.WelcomeStart() # 显示Logo
    SelfCheck.LibCheck()
    print(Colors.BLUE + Logo.div_line_n_m + Colors.END + "\n")
    while True:
        try:
            IceShell()
        except KeyboardInterrupt:
            print("\nBye~")
            exit(0)

