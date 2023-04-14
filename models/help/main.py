import sys
sys.path.append("../../")

from tools.iPrint import *

# 读取配置文件
# 格式：print=a function which print "helloworld"
def read_man_conf():
    with open("../man.conf", "r") as f:
        conf = f.read()
    
    conf = conf.split("\n")
    conf_dict = {}
    author_dict = {}
    for line in conf:
        if line != "":
            line = line.split("=")
            aut = line[1].split("%%")
            conf_dict[line[0]] = aut[0]
            author_dict[line[0]] = aut[1]
    return conf_dict, author_dict

config, author = read_man_conf()

# 打印帮助信息
print("Man Help\tAuthor\tMan")
print('--------------------------------------')
for man in config:
    print(f"{man}\t\t{author[man]}\t{config[man]}")

