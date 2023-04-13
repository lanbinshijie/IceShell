from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("echo", help="add some")
args = parser.parse_args()
echo = args.echo
print(echo)