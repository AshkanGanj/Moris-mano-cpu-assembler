import struct
from file_opr import write_file

def compiler(object_dict, output_path, mode):
    header_list = list(object_dict.keys())
    #sort dic keys
    header_list.sort()
    for memory_location in header_list:
        integer = int(object_dict[memory_location], 16)
        # update values to bin
        object_dict[memory_location] = struct.pack('>i', integer)
    write_file(output_path, header_list, object_dict, mode)