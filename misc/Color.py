#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : Cr4y0n
# @Software: PyCharm
# @Time    : 2020/8/16 8:09

"""
RED ：报错、错误信息、失败信息
GREEN ：成功、重要发现
YELLOW ：警告、重要提示
BLUE ：保留
PURPLE ：保留
CYAN ：次要提示
"""

class Colors:
    RED = "\033[91m"
    GREEN = "\033[32m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    END = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    def colorTestPrint(self):
        print(Colors.RED + "RED" + Colors.END)
        print(Colors.GREEN + "GREEN" + Colors.END)
        print(Colors.YELLOW + "YELLOW" + Colors.END)
        print(Colors.BLUE + "BLUE" + Colors.END)
        print(Colors.PURPLE + "PURPLE" + Colors.END)
        print(Colors.CYAN + "CYAN" + Colors.END)
