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
        uninstall = []
        for lib in ProgramInfo.using_libs:
            total += 1
            try: 
                __import__(lib)
                success += 1
            except: 
                iPrintLog("Importing Lib \""+lib+"\" Error.", processName="SelfCheck", modelName="Import", typer="error")
                uninstall.append(lib)
                error += 1
        iPrintLog(f"Libs Check Finish. {total} in total, {success} success, {error} error. ", processName="SelfCheck", modelName="Import", typer="success")
        if error > 0:
            iPrintLog("检测到有依赖库未安装，请按照上方提示安装对应库！", processName="SelfCheck", modelName="Import", typer="info")
            iPrintLog("您可以通过运行downlib来安装这些模块。", processName="SelfCheck", modelName="Import", typer="info")
            iPrintLog("是否前往安装？ “Y”前往IShell / “N”手动安装", processName="SelfCheck", modelName="Import", typer="info")
            ans = input(Colors.RED + "您的输入：> " + Colors.END)
            if ans == "Y":
                iPrintLog("为了避免不必要的报错，请您立刻运行downlib命令安装依赖库！", processName="SelfCheck", modelName="Import", typer="warning")
                return
            else:
                exit(0)
        else:
            iPrintLog("您可以正常运行本程序！", processName="SelfCheck", modelName="Import", typer="info")
            SelfCheck.ModelCheck()

    
    def ModelCheck():
        if "*" in ProgramInfo.registered_modules:
            iPrintLog("模块注册包含通配符\"*\"，请不要在生产环境中使用！", processName="SelfCheck", modelName="Model", typer="warning")
        if ProgramInfo.debug_mode:
            iPrintLog("开发者模式开启！", processName="SelfCheck", modelName="Debug", typer="warning")
    
    def LibCheckNative():
        uninstall = []
        for lib in ProgramInfo.using_libs:
            try: 
                __import__(lib)
            except: 
                uninstall.append(lib)
        return uninstall
    
    def CheckModel(modelName):
        # iPrintLog("Checking model \""+modelName+"\"...", processName="SelfCheck", modelName="Models", typer="info")
        if os.path.exists(ProgramInfo.models_path + modelName +".py"):
            # iPrintLog("Model \""+modelName+"\" is exists. ", processName="SelfCheck", modelName="Models", typer="success")
            return True
        elif os.path.exists(ProgramInfo.models_path + modelName + "/main.py"):
            return True
        else:
            iPrintLog("Model \""+modelName+"\" is NOT exists! Please Check `main.py` and `"+ modelName +".py`", processName="SelfCheck", modelName="Models", typer="error")
            return False

