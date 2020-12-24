from file_opr import cleaner
from assembler import *
from pre_compile import precompile
from compiler import compiler

output_file = "./output.txt"
# select type of out put b for binary and t for txt
mode = "t"


def run():
    # read code from input file
    source = readFile("./input.txt")
    # make code cleaner
    source = cleaner(source)
    # convert to list of strings
    lines = toList(source)
    # first phase
    symbols_address = precompile(source)
    # second pahse
    obj_dict = assembler(lines, symbols_address)
    # write to file and convert to binary
    compiler(obj_dict, output_file, mode)

    print('\n Compiled successfully\n')
    print('\n Saved as Output.txt \n')


if __name__ == "__main__":
    run()
