import os,argparse
parser = argparse.ArgumentParser()
parser.add_argument('arg1',type=int, help=('display a integer'))
args = parser.parse_args()
print(vars(args))
print(args.arg1)
