import argparse
import sys

from src import Errors

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

class Ev:


    def ev(self, s):
        # s = self.s
        self.toks = s.split()
        self.stack = []
        self.ev_expr(self, s)

    def ev_expr(self, s):
        toks = s.split()
        stack = []
        try:
            for tok in toks:
                if tok.isdigit(): stack.append(tok)
                elif tok=='+':
                    rhs = int(stack.pop())
                    lhs = int(stack.pop())
                    stack.append(lhs+rhs)
                elif tok=='-':
                    rhs = int(stack.pop())
                    lhs = int(stack.pop())
                    stack.append(lhs-rhs)
                elif tok=='/':
                    rhs = int(stack.pop())
                    lhs = int(stack.pop())
                    stack.append(lhs/rhs)
                elif tok == '*':
                    rhs = int(stack.pop())
                    lhs = int(stack.pop())
                    stack.append(lhs * rhs)
                elif tok == 'print':
                    item = stack.pop()
                    stack.append(item)
                    print(item)
        except IndexError:
          raise SyntaxError("Please fulfil all arguments for a function") from None
        except Exception as e:
            raise Errors.UnknownError(e) from e


if __name__ == '__main__':
    Ev.ev(Ev, open(args.file).read())