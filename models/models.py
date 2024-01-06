import os
import sys
import argparse
import re

sys.path.append("..")

from tools.iPrint import iPrintLog
from misc.Info import ProgramInfo
from misc.Logo import Logo

class DisplayAllModules:
    def __init__(self):
        self.lists = os.listdir(".")
        self.model_info = {}

    def filter_lists(self):
        # 保留所有后缀名为.py的文件或者不以'__'开头的文件夹
        self.lists = [i for i in self.lists if i.endswith(".py") or ("." not in i and not i.startswith("__"))]
        for i in range(len(self.lists)):
            if not self.lists[i].endswith(".py"):
                self.lists[i] += "/main.py"

    def parse_plugin_info(self):
        # 获取插件信息
        for i in range(len(self.lists)):
            with open(self.lists[i], "r", encoding="utf-8") as f:
                content = f.read()
                if content.startswith("#! IcePlugin.v1"):
                    plugin_name = content.split("PluginName: ")[1].split("\n")[0]
                    author = content.split("Author: ")[1].split("\n")[0]
                    description = content.split("Description: ")[1].split("\n")[0]
                    version = content.split("Version: ")[1].split("\n")[0]
                    last_edit = content.split("LastEdit: ")[1].split("\n")[0]
                    self.model_info[self.lists[i]] = {
                        "name": plugin_name,
                        "author": author,
                        "description": description,
                        "version": version,
                        "last_edit": last_edit,
                    }

    def display_all(self):
        print("\nModels Found\t\tAuthor")
        print(Logo.div_line_n)
        for it in self.lists:
            tabs = "\t\t\t" if len(it) < 8 else "\t\t"
            author = self.model_info.get(it, {}).get("author", "None")
            print(f"{it}{tabs}{author}")

        print("\nCommands Found\t\tAuthor")
        print(Logo.div_line_n)
        for it in ProgramInfo.registered_modules:
            if it != "*":
                print(f"{it}\t\t\tNone")
        print()
        total_model = len(self.lists)
        if total_model == 0:
            iPrintLog("No models were found.", modelName="models", typer="error")
            return
        if len(ProgramInfo.registered_modules)-int("*" in ProgramInfo.registered_modules) == total_model:
            # 注册的模型数量与实际模型数量相等
            iPrintLog(f"Found {total_model} models. And {len(ProgramInfo.registered_modules)-1} models were registered.", modelName="models", typer="success")
        else:
            iPrintLog(f"Found {total_model} models. But only {len(ProgramInfo.registered_modules)} models were registered.", modelName="models", typer="warning")


def add_spaces_for_chinese_characters(value):
    # 使用正则表达式找到所有中文字符
    chinese_characters = re.findall(r'[\u4e00-\u9fff]', value)
    num_chinese_characters = len(chinese_characters)

    # 在字符串后面添加相应数量的空格
    return value + '1' * num_chinese_characters

def display_module_info(input_name, all_modules):
    found = False
    input_name_lower = input_name.lower()
    
    # 检查是否有匹配的模块（不区分大小写）
    for path, info in all_modules.model_info.items():
        name_lower = info['name'].lower()
        path_lower = path.lower()
        if name_lower == input_name_lower or path_lower.endswith(input_name_lower + '.py'):
            found = True
            # 以表格形式打印信息
            print(f"+{'-'*18}+{'-'*40}+")
            print(f"| {'Attribute':^16} | {'Value':^38} |")
            print(f"+{'-'*18}+{'-'*40}+")
            for key, value in info.items():
                value = add_spaces_for_chinese_characters(value)
                print(f"| {key.capitalize():<16} | {value:<38} |")
            print(f"+{'-'*18}+{'-'*40}+")
            break

    if not found:
        # print(f"Module '{input_name}' not found.")
        print(f"+{'-'*18}+{'-'*40}+")
        print(f"| {'Attribute':^16} | {'Value':^38} |")
        print(f"+{'-'*18}+{'-'*40}+")
        key = "Error"
        value = "Module doesn't exsist or has no MetaInfo."
        print(f"| {key.capitalize():<16} | {value:<38} |")
        print(f"+{'-'*18}+{'-'*40}+")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("module", nargs="?", help="Module name or path to display its information.")
    args = parser.parse_args()

    all_modules = DisplayAllModules()
    all_modules.filter_lists()
    all_modules.parse_plugin_info()

    if args.module:
        display_module_info(args.module, all_modules)
    else:
        all_modules.display_all()

if __name__ == "__main__":
    main()
    iPrintLog(f"Models end!", modelName="models", typer="info")
