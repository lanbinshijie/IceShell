#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : Lanbin
# @Software: Vscode
# @Time    : 2023-1-13 14:18

import os

class ProgramInfo:
    # Program Version
    version = "v1.0.0-alphav1.2.1"
    author = "Lanbin"
    using_libs = ["os", "sys"]
    models_path = r"./models/"
    registered_modules = ["print", "downlib", "dellib", "scan", "models", "shell", "alias", "bash", "*"]
    debug_mode = True
    ssr_path = r"./ssr/"
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))).replace("\\", "/")

class SSR_Reader:
    # Shell System Resource Reader
    # 用来读取IceShell的配置文件和调用的系统资源信息
    # 主要是配置
    
    # Init 函数，检查ProgramInfo中对应的配置文件是否存在，如果不存在则创建
    # 地址为ProgramInfo.ssr_path
    def __init__(self):
        # 检查配置文件夹是否存在
        if not os.path.exists(ProgramInfo.ssr_path):
            os.mkdir(ProgramInfo.ssr_path)
        # 检查配置文件是否存在
        if not os.path.exists(ProgramInfo.ssr_path + "config.ssr"):
            with open(ProgramInfo.ssr_path + "config.ssr", "w") as f:
                # 写入默认配置（如现在ProgramInfo中的配置）
                # 写入的内容要用双引号括起来，这样读取时可以直接eval
                f.write("version=\"" + ProgramInfo.version + "\"\n")
                f.write("author=\"" + ProgramInfo.author + "\"\n")
                f.write("using_libs=" + str(ProgramInfo.using_libs) + "\n")
                f.write("models_path=\"" + ProgramInfo.models_path + "\"\n")
                f.write("registered_modules=" + str(ProgramInfo.registered_modules) + "\n")
                f.write("debug_mode=" + str(ProgramInfo.debug_mode) + "\n")
                f.write("ssr_path=\"" + ProgramInfo.ssr_path + "\"\n")

        # 读取配置文件
        self.config = self.paraphraser(ProgramInfo.ssr_path + "config.ssr")
        # 更新配置
        # self.update_config()


    # 解码器：将配置文件中的格式转化成字典
    # 格式示例（都是合法的）：
    # key=value
    # key = value
    # 请注意，“#”是注释符号，不会被解析，一般独占一行的开头
    # 请注意，如果value中有“=”号，那么value中的“=”号不会被解析为=号而是作为普通字符

    def paraphraser(self, config_file: str = ProgramInfo.ssr_path + "config.ssr"):
        # 返回值：配置字典
        # 读取文件
        with open(config_file, "r") as f:
            config = f.read()
        # 解析文件
        config = config.split("\n")
        config_dict = {}
        for line in config:
            if line != "":
                if line[0] != "#":
                    line = line.split("=")
                    # 去除空格
                    line[0] = line[0].strip()
                    line[1] = line[1].strip()
                    # 添加到字典
                    config_dict[line[0]] = eval(line[1])
        return config_dict

    # 写入器：将字典写入配置文件
    def writer(self, config_file: str, config_dict: dict):
        # 返回值：Bool 是否成功
        # 捕捉错误
        try:
        # 打开文件
            with open(config_file, "w") as f:
                # 写入
                for key in config_dict:
                    f.write(key + "=" + config_dict[key] + "\n")
            return True
        except:
            return False


class StartAction:
    def __init__(self, path):
        self.grub = ProgramInfo.basedir + "/ssr/" + path
    def return_action(self):
        with open(self.grub, "r") as f:
            return f.read()



