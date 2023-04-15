# Ish 执行模块
# 功能：执行一个.sh文件中的所有命令
# 语法参见：ish语法.md

import os
import sys

sys.path.append("..")

from argparse import ArgumentParser
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
            # 新建一个argparse的参数解析器，解析path参数
            parser = ArgumentParser()
            parser.add_argument("path", help="要执行的.sh文件路径")
            args = parser.parse_args()

            # 读取文件
            with open(args.path, "r", encoding="utf-8-sig") as f:
                for line in f.readlines():
                    self.run_file(line)

        except EOFError:
            print("\nBye~")
            exit(0)
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
            # 跳过空行
            if line == "":
                continue
            if line[0] == "#" or line[0] == ";":
                continue # 跳过注释
            elif line[0] == "$":
                variable = line.split("=")
                variable[0] = variable[0][1:] # 去掉$符号
                # 去掉两个首尾的空格（如：$ var = 100）
                variable[0] = variable[0].strip()
                variable[1] = variable[1].strip()
                self.var_define(variable[0], self.replace_var(variable[1]))
            else:
                if line_split[0] in self.commands:
                    self.commands[line_split[0]](line_split[1:])
                else:
                    # 当没有内置命令时，执行模块，传入参数
                    # ExecuteModel(line_split[1:], line_split[0])
                    print("".join(line_split[1:]), line_split[0])
                    ExecuteModel("".join(line_split[1:]), line_split[0])

    def fun_echo(self, args):
        # print("||".join(args))
        for arg in args:
            # 当参数为变量时，输出变量的值
            print(self.deal_var(arg), end=" ")
        print()
    

    def deal_var(self, var):
        # 返回一个式子的值（先判断是否是变量，再判断是否是列表，最后判断是否是字典）
        # 如果一个变量什么都不加，就是直接输出变量的值
        # 列表：$var->index
        # 字典：$var->key
        if self.is_var(var):
            # 变量名要去除前面的$
            var = var[1:]
            # print("var",var)
            if "->" in var:
                var = var.split("->")
                if var[0] in self.variables:
                    if type(self.var_call(var[0])) == list:
                        return self.read_list(var[0], int(var[1]))
                    elif type(self.var_call(var[0])) == dict:
                        return self.read_dict(var[0], var[1])
                    else:
                        return self.var_call(var[0])
                else:
                    return var
            else:
                return self.var_call(var)
        else:
            return var
        

    # 替换一个命令中的所有变量为它的值，然后返回计算结果
    def replace_var(self, command):
        # 替换所有$开头的变量
        for var in self.variables:
            command = command.replace("$" + var, str(self.var_call(var)))
        # 计算表达式的值
        return eval(command)
    
    # 当变量是列表时，读取列表中的值
    def read_list(self, var, index):
        return self.var_call(var)[index]
    
    # 当变量是字典时，读取字典中的值
    def read_dict(self, var, key):
        return self.var_call(var)[key]
    
    # 识别是否是一个变量
    def is_var(self, var):
        if var[0] == "$":
            return True
        else:
            return False
        
    # 识别是否是一个列表
    def is_list(self, var):
        if var[0] == "[" and var[-1] == "]":
            return True
        else:
            return False
        
    # 识别是否是一个字典
    def is_dict(self, var):
        if var[0] == "{" and var[-1] == "}":
            return True
        else:
            return False

if __name__ == "__main__":
    Ish()