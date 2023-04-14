
import os
import sys

sys.path.append("..")

from tools.iPrint import *

from argparse import ArgumentParser
from misc.Info import ProgramInfo
from misc.Logo import Logo

lists = os.listdir(".")

# 剔除lists中所有后缀名非.py的文件并保持原格式
lists = [i for i in lists if i.endswith(".py")]

total_model = len(lists)

print("\nModels Found"+"\t\t"+"Author")
print(Logo.div_line_n)

for it in lists:
    print(it+"   "+"\t\t"+"None")

print()

print("\nCommands Found"+"\t\t"+"Author")
print(Logo.div_line_n)

for it in ProgramInfo.registered_modules:
    if it != "*":
        print(it+"     "+"\t\t"+"None")
print()

if len(ProgramInfo.registered_modules)-int("*" in ProgramInfo.registered_modules) == total_model:
    iPrintLog(f"Found {total_model} models. And {len(ProgramInfo.registered_modules)-1} models were registered.", modelName="models", typer="success")
else:
    iPrintLog(f"Found {total_model} models. But {len(ProgramInfo.registered_modules)} models were registered.", modelName="models", typer="warning")
iPrintLog(f"Models end!", modelName="models", typer="info")
