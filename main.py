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
from misc.Info import SSR_Reader
from misc.Error import Error
from tools.Phraser import PS1
from tools.Phraser import alias
from misc.Info import StartAction
# from models.bash import Ish

ALIAS = alias()
# ish = Ish()

def ExecuteModel(args, moduleName):
    if SelfCheck.CheckModel(moduleName):
        os.chdir(rf"{ProgramInfo.basedir}/models")
        if os.path.exists(f"{moduleName}.py"):
            command = sys.executable + f" ./{moduleName}.py " + args
        elif os.path.exists(f"./{moduleName}/main.py"):
            os.chdir(rf"./{moduleName}")
            command = sys.executable + f" ./main.py " + args
        else:
            if ALIAS.exsist(moduleName): 
                command = ALIAS.get(moduleName)
                command = sys.executable + f" ./{command}.py " + args
        os.system(command)
        os.chdir(rf"{ProgramInfo.basedir}")
    # elif moduleName in
    else:
        # print()
        ...

def IceShell():
    extra = ""
    commandN = input(Colors.RED + extra + PS1.paraphraser() + Colors.END)
    command = commandN.split(" ")
    if command[0] == "q":
        print("Bye~")
        exit(0)
    elif command[0] in ProgramInfo.registered_modules or "*" in ProgramInfo.registered_modules:
        ExecuteModel(" ".join(command[1:]), command[0])
    else:
        Error.printError(10000)

if __name__ == "__main__":
    # 程序从这里开始
    SelfCheck.WelcomeStart() # 显示Logo
    SelfCheck.LibCheck()

    ssr = SSR_Reader()
    startup_name = "startup.ish"
    mdls_stp = "../ssr/" + startup_name
    mfol_stp = "./ssr/" + startup_name
    if os.path.exists(mfol_stp):
        ExecuteModel(mdls_stp, "bash")
    print(Colors.BLUE + Logo.div_line_n_m + Colors.END + "\n")

    while True:
        try:
            IceShell()
        except KeyboardInterrupt:
            print("\nBye~")
            exit(0)

