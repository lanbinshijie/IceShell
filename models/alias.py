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

aliases = ALIAS.getAll()
print("Alias\tRunable")
print('----------------')
for i in aliases:
    print(f"{i}\t-> {aliases[i]}")

