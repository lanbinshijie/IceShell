#! IcePlugin.v1
#! PluginName: Calculator
#! Author: Lanbin
#! Description: A simple calculator
#! Version: 1.0.0
#! LastEdit: 2024-1-7 00:05:41

while True:
    a = input(">>> ")
    if a == "q":
        print("Bye~")
        exit(0)
    print(eval(a))