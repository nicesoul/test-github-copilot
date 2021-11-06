# main file for actual coding

# import modules from other subfolders
import sys
sys.path.insert(0, '.')

from utils.terminal_colors import Terminal_colors as colors


def main():
    """
    Docstring here
    """
    print(f'{colors.yellow}Good luck, Have fun!{colors.grey}')
    print(f'{colors.color_check(colors)}')


if __name__ == '__main__':
    main()
