#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : Lanbin
# @Software: Vscode
# @Time    : 2023-1-13 14:45

from misc.Color import Colors

def iPrint_Error(text: str):
    return Colors.RED + text + Colors.END

def iPrint_Success(text: str):
    return Colors.GREEN + text + Colors.END

def iPrint_Warning(text: str):
    return Colors.YELLOW + text + Colors.END

def iPrint_Notice(text: str):
    return Colors.CYAN + text + Colors.END

def iPrint_Info(text: str):
    return Colors.BLUE + text + Colors.END

def iPrint_Bold(text: str):
    return Colors.BOLD + text + Colors.END

def iPrintLog(text: str, processName="IShell",modelName="Main",typer:str ="info"):
    print(iPrint(f"[{processName}][{modelName}][{typer.upper()}] {text}", typer))

def iPrintLogNative(text: str, processName="IShell",modelName="Main",typer:str ="info"):
    print(iPrint(f"[{processName}][{modelName}][{typer.upper()}] {text}", typer), end="")

def iPrint(text: str, typer: str, bold: bool = False):
    res = text
    if typer == "error": res = iPrint_Error(res)
    elif typer == "success": res = iPrint_Success(res)
    elif typer == "warning": res = iPrint_Warning(res)
    elif typer == "notice": res = iPrint_Notice(res)
    elif typer == "info": res = iPrint_Info(res)
    if bold: res = iPrint_Bold(res)
    return res

