import sys,os
from argparse import ArgumentParser
pa = os.getcwd()
sys.path.append("..")

from tools.Phraser import alias

os.chdir(pa+r"\..\tools")
ALIAS = alias("alias.conf")
from misc.Info import ProgramInfo

class Aliaser:
    """
    This class manages command aliases stored in a configuration file.
    """
    def __init__(self, path=ProgramInfo.basedir + "/tools/alias.conf"):
        self.path = path
        self.alias = alias(path)

    def _update_file(self, config):
        """Writes the updated configuration to the file."""
        with open(self.path, "w") as f:
            for alias, command in config.items():
                f.write(f"{alias}={command}\n")

    def add(self, alias, command):
        """Adds a new alias."""
        if self.alias.exist(alias):
            print(f"Alias {alias} already exists!")
            return
        with open(self.path, "a") as f:
            f.write(f"\n{alias}={command}")

    def set(self, alias, command):
        """Sets an existing alias to a new command."""
        if not self.alias.exist(alias):
            print(f"Alias {alias} does not exist!")
            return
        config = self.alias.getAll()
        config[alias] = command
        self._update_file(config)

    def delete(self, alias):
        """Deletes an existing alias."""
        if not self.alias.exist(alias):
            print(f"Alias {alias} does not exist!")
            return
        config = self.alias.getAll()
        del config[alias]
        self._update_file(config)

def print_aliases(aliases):
    """Prints all available aliases."""
    print("Alias\tRunable")
    print('----------------')
    for alias, command in aliases.items():
        print(f"{alias}\t-> {command}")

def main():
    parser = ArgumentParser()
    parser.add_argument("-a", "--add", help="Add a new alias in the format alias=command")
    parser.add_argument("-s", "--set", help="Set an existing alias to a new command")
    parser.add_argument("-d", "--delete", help="Delete an existing alias")
    parser.add_argument("-f", "--flush", action="store_true", help="Flush alias configuration")

    args = parser.parse_args()
    aliaser = Aliaser()

    if args.flush:
        aliaser.alias.reRead()
        return

    if args.add:
        alias, command = args.add.split("=")
        aliaser.add(alias, command)
    elif args.set:
        alias, command = args.set.split("=")
        aliaser.set(alias, command)
    elif args.delete:
        aliaser.delete(args.delete)
    else:
        print_aliases(aliaser.alias.getAll())
        return

    # Refresh and display updated aliases
    aliaser.alias.reRead()
    print_aliases(aliaser.alias.getAll())

if __name__ == "__main__":
    main()
