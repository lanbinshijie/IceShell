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

for i in range(len(lists)):
    if not lists[i].endswith(".py"):
        lists[i] += "/main.py"


# 获取插件信息
model_info = {}
#! IcePlugin.v1
#! PluginName: 
#! Author: 
#! Description: 
#! Version: 
#! LastEdit: 

# 插件元信息如上所示，会放在文件开头，首先识别第一行的 #! IcePlugin.v1 
# 然后根据后面的内容进行解析，如果没有第一行标识符就不用管信息
for i in range(len(lists)):
    # 读取文件内容
    with open(lists[i], "r", encoding="utf-8") as f:
        content = f.read()
        # 解析文件内容
        if content.startswith("#! IcePlugin.v1"):
            # 解析插件信息
            plugin_name = content.split("PluginName: ")[1].split("\n")[0]
            author = content.split("Author: ")[1].split("\n")[0]
            description = content.split("Description: ")[1].split("\n")[0]
            version = content.split("Version: ")[1].split("\n")[0]
            last_edit = content.split("LastEdit: ")[1].split("\n")[0]
            # 存入model_info字典中
            model_info[lists[i]] = {
                "name": plugin_name,
                "author": author,
                "description": description,
                "version": version,
                "last_edit": last_edit,
            }



total_model = len(lists)

# 打印模型信息
print("\nModels Found\t\tAuthor")
print(Logo.div_line_n)

for it in lists:
    # 根据项目名称长度调整制表符
    tabs = "\t\t\t" if len(it) < 8 else "\t\t"
    author = "None"
    if it in model_info:
        author = model_info[it]["author"]
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
