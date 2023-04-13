
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

