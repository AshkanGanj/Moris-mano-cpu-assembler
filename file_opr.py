import os
import struct

def readFile(path):
    if not os.path.isfile(path):
        raise FileNotFoundError
    else:
        with open(path, 'r') as file:
            source = file.read()
            
    return source


def cleaner(source):
    lines = source.split('\n')
    for i in range(len(lines)):
        strings = lines[i].split()
        for string in strings:
            if string[0] == ';':
                index = strings.index(string)
                delete = strings[index:]
                for item in delete:
                    strings.remove(item)
        lines[i] = ' '.join(strings)
    return '\n'.join(lines)


def write_file(path, header, object_dict, mode):

    if mode == 'b':
        with open(path, 'wb+') as output:
            for memory_location in header:
                output.write(object_dict[memory_location])

    elif mode == 't':
        with open(path, 'w+') as output:
            for memory_location in header:
                integer = struct.unpack('>i', object_dict[memory_location])
                integer = integer[0]
                output.write(dectobin(integer, 16) + '\n')


def dectobin(decimal, bits):
    binary = bin(decimal & int("1" * bits, 2))[2:]
    return ("{0:0>%s}" % bits).format(binary)