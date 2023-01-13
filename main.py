import os, sys
from misc.Color import Colors
from misc.Logo import Logo
from tools.SelfCheck import SelfCheck

def ExecuteModel(choice, keyWord, moduleName):
    if not SelfCheck.CheckModel(moduleName): return
    args = choice[len(keyWord):]
    os.chdir(r"./models")
    command = sys.executable + f" ./{moduleName}.py" + args
    os.system(command)
    os.chdir(r"..")

def IceShell():
    extra = ""
    choice = input(Colors.RED + extra + "IShell> " + Colors.END)
    if choice[:5] == "print":
        ExecuteModel(choice, "print", "print")
    elif choice == "0" or choice == "q":
        print("Bye~")
        exit(0)

if __name__ == "__main__":
    # 程序从这里开始
    SelfCheck.WelcomeStart() # 显示Logo
    SelfCheck.LibCheck()
    print(Colors.BLUE + Logo.div_line_n_m + Colors.END + "\n")
    while True:
        try:
            IceShell()
        except KeyboardInterrupt:
            print("\nBye~")
            exit(0)

    
