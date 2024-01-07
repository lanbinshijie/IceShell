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
from tools.Configure import *
# from models.bash import Ish



ALIAS = alias()
PS1O = PS1()
CONFIGURATION = Configuration()
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
        # 因为 checkModel 会给出提示信息，所以就不用给出了
        ...

def SafetyMode(lock):
    if int(lock):
        print(Colors.RED + Logo.div_line_n_m + Colors.END)
        print(Colors.RED + "Safety Mode is on." + Colors.END)
        print(Colors.RED + "Please input your password to continue." + Colors.END)
        print(Colors.RED + Logo.div_line_n_m + Colors.END + "\n")

        while True:
            try:
                userName = input("Username: >> ")
                password = input("Password: >> ")
                passwordHashed = Hash(password)
                if userName == CONFIGURATION.userName and passwordHashed == str(CONFIGURATION.passwordHashed).split("%%")[0]:
                    print()
                    print(Colors.GREEN + Logo.div_line_n_m + Colors.END)
                    print(Colors.GREEN + "Welcome back, " + userName + "!" + Colors.END)
                    print(Colors.GREEN + Logo.div_line_n_m + Colors.END + "\n")
                    break
                else:
                    print()
                    print(Colors.RED + Logo.div_line_n_m + Colors.END)
                    print(Colors.RED + "Wrong username or password!" + Colors.END)
                    print(Colors.RED + Logo.div_line_n_m + Colors.END + "\n")
                    continue
            except KeyboardInterrupt:
                print("\nBye~")
                exit(0)

def IceShell():
    extra = ""
    commandN = input(Colors.RED + extra + PS1.paraphraser() + Colors.END)
    command = commandN.split(" ")
    SECLEVEL = 0
    if command[0] == "q":
        print("Bye~")
        exit(0)
    elif CONFIGURATION.ifexist(str(commandN.split("=")[0]).strip()[1:]) and commandN.startswith("$"):
        conf = commandN.split("=")
        conf = [str(item).strip() for item in conf]
        conf[0] = conf[0][1:]
        sec = CONFIGURATION.get(conf[0]).split("%%") # 安全等级，如果越大，需要的等级越高
        sec = int(sec[1]) if len(sec) > 1 else 0
        if sec > SECLEVEL:
            Error.printError(30001)
            print()
            return
        if len(conf) == 2:
            CONFIGURATION.set_value(conf[0], conf[1])
            CONFIGURATION.save()
            print(Colors.GREEN + "Configuration saved." + Colors.END)
        elif len(conf) == 1:
            print(CONFIGURATION.get(conf[0]))
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
    pass_ = SafetyMode(CONFIGURATION.lock)
    while True:
        try:
            IceShell()
        except KeyboardInterrupt:
            print("\nBye~")
            exit(0)

