
import os
import sys

sys.path.append("..")

from tools.iPrint import *

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("libname", help="The name of the lib which you want to delete.")
args = parser.parse_args()
if args.libname == None:
    iPrintLog("Nothing to delete", "Dellib", "Main", "warning")
    exit(0)

try:
    os.system("pip uninstall "+args.libname)
except:
    iPrintLog("Deleting error!", "Dellib", "Main", "error")
