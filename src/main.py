import argparse
import sys

ver = '1.0.0'

parser = argparse.ArgumentParser(
                    prog='H20',
                    description='A simple interpreter for the H20 language',
                    epilog=f'H20 V{ver}')

parser.add_argument('file')           # positional argument
# parser.add_argument('-c', '--count')      # option that takes a value
# parser.add_argument('-v', '--verbose',
#                     action='store_true')  # on/off flag
args = parser.parse_args()
def ev(s):
    toks = s.split()
    stack = []
if __name__ == '__main__':
    ev(open(args.file).read())