import getopt
import importlib
import sys

unix_options = ['hd:p:']
gnu_options = ['help', 'day=', 'part=']

help_string = '''
Advent of Code 2019 Helper Script 🎅

In order for this script to work, you *must* insert at least a day.

If you enter both a day and a part, the script will run that particular day and part. Otherwise, if you only enter a 
day, it will show you both parts for that day. 

--help, -h  ::  Show instructions & cmd options available
--day, -d   ::  Select the day you would like to run
--part, -p  ::  Select the part of the day you would like to run
'''


def get_solution(day, part):
    module_string = f'adventofcode2019.day{day}.part{part}'
    try:
        solution = importlib.import_module(module_string)
    except ImportError:
        print(f'I am not able to find the module for Day {day}, Part {part}')
        print('Are you sure they have been completed?')

    return solution.solve()


if __name__ == '__main__':
    print('🎅🦌 Advent of Code 2019 🦌🎅')
    arg_list = sys.argv[1:]

    try:
        arguments, values = getopt.getopt(arg_list, unix_options, gnu_options)
    except getopt.error as err:
        print(str(err))
        sys.exit(2)

    day_input = 0
    part_input = 0

    for current_arg, current_value in arguments:
        if current_arg in ('-h', '--help'):
            print(help_string)
            sys.exit(0)
        elif current_arg in ('-d', '--day'):
            day_input = int(current_value)
        elif current_arg in ('-p', '--part'):
            part_input = int(current_value)

    if not day_input:
        print('You must select at least a day. Use --help for more info.')
        print(f'    Day: {day_input}')
        print(f'    Part: {part_input}')
    elif day_input > 25 or part_input > 2:
        print('You must select a day from 1 to 25, and either 1 or 2 for part.')
        print(f'    Day: {day_input}')
        print(f'    Part: {part_input}')
    elif day_input and not part_input:
        day_str = str(day_input).zfill(2)
        print(f'Only a day was selected. Running all parts for Day {day_input}...')
        for r in [1, 2]:
            print(f'    Part {r}: {get_solution(day_str, r)}')
    else:
        day_str = str(day_input).zfill(2)
        part_str = str(part_input)
        print(f'Running for Day {day_str.zfill(2)}, Part {part_str}')
        print(f'    {get_solution(day_str, part_str)}')
