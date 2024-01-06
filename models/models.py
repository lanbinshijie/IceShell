import os
import sys

sys.path.append("..")

from tools.iPrint import iPrintLog
from misc.Info import ProgramInfo
from misc.Logo import Logo

# 获取当前目录下的文件列表
lists = os.listdir(".")

# 保留所有后缀名为.py的文件或者不以'__'开头的文件夹
lists = [i for i in lists if i.endswith(".py") or ("." not in i and not i.startswith("__"))]

total_model = len(lists)

# 打印模型信息
print("\nModels Found\t\tAuthor")
print(Logo.div_line_n)

for it in lists:
    if not it.endswith(".py"):
        it = it + "/main.py"
    # 根据项目名称长度调整制表符
    tabs = "\t\t\t" if len(it) < 8 else "\t\t"
    author = "None"
    print(f"{it}{tabs}{author}")

print("\nCommands Found\t\tAuthor")
print(Logo.div_line_n)

for it in ProgramInfo.registered_modules:
    if it != "*":
        author = "None"
        print(f"{it}\t\t\t{author}")
print()

if len(ProgramInfo.registered_modules)-int("*" in ProgramInfo.registered_modules) == total_model:
    # 注册的模型数量与实际模型数量相等
    iPrintLog(f"Found {total_model} models. And {len(ProgramInfo.registered_modules)-1} models were registered.", modelName="models", typer="success")
else:
    iPrintLog(f"Found {total_model} models. But {len(ProgramInfo.registered_modules)} models were registered.", modelName="models", typer="warning")
iPrintLog(f"Models end!", modelName="models", typer="info")
