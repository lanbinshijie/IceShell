
# 字符替换工具

from misc.Info import ProgramInfo

class PS1:
    def paraphraser(prompt="[IShell] %u> "):
        # 返回值：替换后的字符串
        # 将prompt中的特殊字符替换成对应的内容
        # 特殊字符：
        # %n 程序名：默认为IShell
        # %v 版本号：默认为ProgramInfo.version
        # %u 用户：默认为Lanbin

        # 替换
        prompt = prompt.replace("%n", "IShell")
        prompt = prompt.replace("%v", ProgramInfo.version)
        prompt = prompt.replace("%u", "Lanbin")
        return prompt

class alias:
    def __init__(self, path="tools/alias.conf"):
        with open(path, "r") as f:
            conf = f.read()
        
        conf = conf.split("\n")
        self.conf_dict = {}
        self.author_dict = {}
        for line in conf:
            if line != "":
                line = line.split("=")
                self.conf_dict[line[0]] = line[1]

    def get(self, key):
        return self.conf_dict[key]

    def exsist(self, key):
        if key in self.conf_dict:
            return True
        else:
            return False
    
    def getAll(self):
        self.reRead()
        return self.conf_dict
    
    def reRead(self, path="../tools/alias.conf"):
        with open(path, "r") as f:
            conf = f.read()
        
        conf = conf.split("\n")
        self.conf_dict = {}
        self.author_dict = {}
        for line in conf:
            if line != "":
                line = line.split("=")
                self.conf_dict[line[0]] = line[1]