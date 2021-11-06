# import os     # Miscellaneous operating system interfaces
# os.system('') # Execute the command(a string) in a subshell

class Terminal_colors():
    """
    8 terminal colors based on ANSI escape sequences.
    Values are black, red, green, yellow, blue, violet, cyan, grey.
    Usage of colors should always be returned to grey afterwards.
    Example: print(f'{yellow}I am Yellow{grey}')
    """
    reset_style = '\033[0m'
    colors = []
    for i in range(30, 38):
        colors.append('\033[' + str(i) + 'm')
    black, red, green, yellow, blue, violet, cyan, grey = colors

    def color_check(self):
        for i in self.colors:
            print(i + 'color')
