# importing required modules
import argparse

# create a parser object
parser = argparse.ArgumentParser(description='An concatenation program')

# add argument
parser.add_argument('-s', '--select', action='store_true', help="go to the select a program screen")
parser.add_argument('strs', nargs='*', metavar='str', type=str,
                    help='All strings will be concatenated')

# parse the arguments from standard input
args = parser.parse_args()

# check if add argument has any input data.
# If it has, then print sum of the given numbers
if args.select:
    import survey  # pip install survey

    program_list = ['vs', 'vscode', 'pycharm', 'intelliJ']

    index = survey.routines.select('Favorite IDE? ', options=program_list, focus_mark='> ',
                                   evade_color=survey.colors.basic('blue'))
else:
    if len(args.strs) != 0:
        for string in args.strs:
            print(string, end="")
