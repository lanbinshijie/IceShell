import sys,os
from argparse import ArgumentParser
pa = os.getcwd()
sys.path.append("..")

from tools.Phraser import alias

os.chdir(pa+r"\..\tools")
ALIAS = alias("alias.conf")

# parser = ArgumentParser()
# parser.add_argument("add", help="add some")
# args = parser.parse_args()
# ip = args.add
# start_port = int(args.sp)
# end_port = int(args.np)

# 获取参数
# 如果没有任何参数则输出所有别名
# 参数有三种：add, set, del
# add: 添加别名
# set: 修改别名
# del: 删除别名
# flu: 刷新别名配置文件
# 创建一个类来实现

class Aliaser:
    def __init__(self, path="alias.conf"):
        self.path = path
        self.alias = alias(path)

    def add(self, alias, command):
        if self.alias.exsist(alias):
            print(f"Alias {alias} already exsist!")
        else:
            with open(self.path, "a") as f:
                f.write(f"\n{alias}={command}")

    def set(self, alias, command):
        if self.alias.exsist(alias): # 别名存在
            config = self.alias.getAll()
            config[alias] = command
            with open(self.path, "w") as f:
                for i in config:
                    f.write(f"{i}={config[i]}\n")
        else:
            print(f"Alias {alias} not exsist!")

    def delete(self, alias):
        if self.alias.exsist(alias):
            config = self.alias.getAll()
            del config[alias]
            with open(self.path, "w") as f:
                for i in config:
                    f.write(f"{i}={config[i]}\n")
        else:
            print(f"Alias {alias} not exsist!")
    

# 获取参数 参数可能为空

parser = ArgumentParser()
parser.add_argument("-a", "--add", help="add some")
parser.add_argument("-s", "--set", help="set some")
parser.add_argument("-d", "--delete", help="delete some")
# -f 没有参数，加上即代表刷新
# parser.add_argument("-f", "--flush", help="flush some")
parser.add_argument("-f", "--flush", action="store_true", help="flush some")

args = parser.parse_args()
add = args.add
set = args.set
delete = args.delete
flush = args.flush

# 如果参数为空则输出所有别名
if add == None and set == None and delete == None and flush == False:
    aliases = ALIAS.getAll()
    print("Alias\tRunable")
    print('----------------')
    for i in aliases:
        print(f"{i}\t-> {aliases[i]}")
    exit()

# 如果参数不为空则进行操作
# 如果参数为add则添加别名
# 如果参数为set则修改别名
# 如果参数为del则删除别名
# 如果参数为flu则刷新别名配置文件


if flush:
    ALIAS.reRead()
    exit()

# 如果参数为其他则报错
if add != None:
    add = add.split("=")
    aliaser = Aliaser()
    aliaser.add(add[0], add[1])
    ALIAS.reRead()
elif set != None:
    set = set.split("=")
    aliaser = Aliaser()
    aliaser.set(set[0], set[1])
    ALIAS.reRead()
elif delete != None:
    aliaser = Aliaser()
    aliaser.delete(delete)
    ALIAS.reRead()
else:
    print("Wrong parameter!")
    exit()

aliases = ALIAS.getAll()
print("Alias\tRunable")
print('----------------')
for i in aliases:
    print(f"{i}\t-> {aliases[i]}")
exit()


