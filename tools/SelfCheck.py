#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : Lanbin
# @Software: Vscode
# @Time    : 2023-1-13 14:29
from misc.Info import ProgramInfo
from misc.Color import Colors
from misc.Logo import Logo
from tools.iPrint import *
import os

class SelfCheck:
    def WelcomeStart():
        print(Colors.CYAN + Logo.normal_logo + Colors.END)
        print(Colors.BLUE + Logo.div_line_b_m + Colors.END)
        print(Colors.BLUE+"Welcome Use IShell...\n"+Colors.END)

    def LibCheck():
        iPrintLog("Start Self Check...", processName="SelfCheck", modelName="Import", typer="info")
        total, success, error = 0,0,0
        for lib in ProgramInfo.using_libs:
            total += 1
            try: 
                __import__(lib)
                success += 1
            except: 
                iPrintLog("Importing Lib \""+lib+"\" Error.", processName="SelfCheck", modelName="Import", typer="error")
                error += 1
        iPrintLog(f"Libs Check Finish. {total} in total, {success} success, {error} error. ", processName="SelfCheck", modelName="Import", typer="success")
        if error > 0:
            iPrintLog("检测到有依赖库未安装，请按照上方提示安装对应库！", processName="SelfCheck", modelName="Import", typer="info")
            exit(0)
        else:
            iPrintLog("您可以正常运行本程序！", processName="SelfCheck", modelName="Import", typer="info")
    
    def CheckModel(modelName):
        iPrintLog("Checking model \""+modelName+"\"...", processName="SelfCheck", modelName="Models", typer="info")
        if os.path.exists(ProgramInfo.models_path + modelName +".py"):
            iPrintLog("Model \""+modelName+"\" is exists. ", processName="SelfCheck", modelName="Models", typer="success")
            return True
        else:
            iPrintLog("Model \""+modelName+"\" is NOT exists! Please Check `main.py` and `"+ modelName +".py`", processName="SelfCheck", modelName="Models", typer="error")
            return False

