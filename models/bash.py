# Ish 执行模块
# 功能：执行一个.sh文件中的所有命令
# 语法参见：ish语法.md

import os
import sys
import time
import json
import random
import requests
import threading
import subprocess

sys.path.append("..")

from misc.Color import Colors
from misc.Logo import Logo
from misc.Info import ProgramInfo
from misc.Info import SSR_Reader
from misc.Error import Error
from tools.Phraser import PS1
from tools.Phraser import alias
from tools.SelfCheck import SelfCheck
from main import ExecuteModel

# ALIAS = alias(path="alias.conf")

# 新建一个Class，每个运行的sh程序都是在这个对象里的

class Ish:
    # 要预留程序定义变量的地方（可以用字典储存）
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.commands = {
            "echo": self.fun_echo,
        }
        self.run()
        # 如 {"var1": "value1", "var2": 100}

    def run(self):
        try:
            command = input(Colors.RED + PS1.paraphraser() + "$ " + Colors.END)
            com = command.split(" ")
            if com[0] == "file":
                with open(com[1], "r", encoding="utf-8-sig") as f:
                    for line in f.readlines():
                        self.run_file(line)
            else:
                self.run_command(command)
        except KeyboardInterrupt:
            print("\nBye~")
            exit(0)
        
    
    # 变量定义
    def var_define(self, var, value):
        self.variables[var] = value
    
    # 变量调用
    def var_call(self, var):
        return self.variables[var]
    
    # 变量赋值
    def var_assign(self, var, value):
        self.variables[var] = value

    # 变量加减乘除
    def var_add(self, var, value):
        self.variables[var] += value

    def var_sub(self, var, value):
        self.variables[var] -= value

    def var_mul(self, var, value):
        self.variables[var] *= value

    def var_div(self, var, value):
        self.variables[var] /= value

    
    # if语句
    def if_statement(self, condition, command):
        if condition:
            ...

    # for语句
    def for_statement(self, start, end, step, command):
        for i in range(start, end, step):
            ...
        return i
    
    # while语句
    def while_statement(self, condition, command):
        while condition:
            ...

    # 函数定义
    def func_define(self, func_name, args, command):
        self.functions[func_name] = {"args": args, "command": command}
        ...

    # 函数调用
    def func_call(self, func_name, args):
        ...

    # 函数删除
    def func_delete(self, func_name):
        self.functions.pop(func_name)

    # 运行命令
    def run_command(self, command):
        commandS = command.split(" ")

        if command[0] in self.commands:
            self.commands[command]()
        else:
            # 当没有内置命令时，执行模块，传入参数
            ExecuteModel(commandS[1:], commandS[0])

    def run_file(self, file):
        file = file.splitlines()
        for line in file:
            line_split = line.split(" ")
            if line[0] == "#" or line[0] == ";":
                continue # 跳过注释
            elif line[0] == "$":
                variable = line.split("=")
                variable[0] = variable[0][1:] # 去掉$符号
                # 去掉两个首尾的空格（如：$ var = 100）
                variable[0] = variable[0].strip()
                variable[1] = variable[1].strip()
                self.var_define(variable[0], eval(variable[1]))
            else:
                if line_split[0] in self.commands:
                    self.commands[line_split[0]](line_split[1:])
                else:
                    # 当没有内置命令时，执行模块，传入参数
                    ExecuteModel(line_split[1:], line_split[0])

    def fun_echo(self, args):
        for arg in args:
            # 当参数为变量时，输出变量的值
            if arg[0] == "$":
                arg = arg[1:]
                print(self.var_call(arg), end=" ")
            else:
                print(arg, end=" ")
        print()

if __name__ == "__main__":
    Ish()