# little explanation here
# 3 different approaches with

# made by nicesoul
# check out the repo here https://github.com/nicesoul/

from src.option_1 import main as op1
from src.option_2 import main as op2
from src.option_3 import main as op3


def main_flow(file: str = 'hi', method: int = 1, stats: bool = False) -> int:
    """
    Main program to do stuff.
    returns 0 if
    returns 1 if
    return -1 if input data are incorrect.
    Possible method values are <1>, <2>, <3>.
    Set stats to True to see.
    """
    file = input("please, provide file name: ")
    print(file)
    method = int(input("please, \
type 1 for the first method\n\
        type 2 for the second method\n\
        type 3 for the third method: "))
    if method == 1:
        print('running method 1')
        op1()
    if method == 2:
        print('running method 2')
        op2()
    if method == 3:
        print('running method 3')
        op3()


if __name__ == "__main__":
    main_flow()
