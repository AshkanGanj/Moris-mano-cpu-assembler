from instruction_set import MRI
from instruction_set import NON_MRI
from instruction_set import PSEUDO
from file_opr import readFile

def toList(source):
    lines = source.split('\n')
    return lines


def assembler(lines, symbols_address):
    
    LC = 0
    obj_dict = dict()

    for line in lines:
        strings = line.split()
        switch = len(strings)
        word = strings[0]
        if switch == 1:
            if word == PSEUDO[3]:
                break
            else:
                obj_dict[LC] = hex(NON_MRI[word])
        elif switch == 2:
            #check for ORG
            if word == PSEUDO[0]:
                LC = int(strings[1])
                continue
            else:
                if word in MRI:
                    obj_dict[LC] = combine(strings, symbols_address, 0, 0)
                elif word in PSEUDO:
                    obj_dict[LC] = num_converter(word, strings[1])
        elif switch == 3:
            state = True
            if word[-1] == ',':
                a = 1
                b = 0
                if strings[1] in PSEUDO[1:3]:
                    state = False
            else:
                a = 0
                b = 1
            if state:
                obj_dict[LC] = combine(strings, symbols_address, a, b)
            else:
                obj_dict[LC] = num_converter(word, strings[2])
        elif switch == 4:
            obj_dict[LC] = combine(strings, symbols_address, 1, 1)
        LC += 1

    return obj_dict

def combine(strings, symbols_address, index1, index2):
    address = symbols_address[strings[index1 + 1]]
    #set 3 bit hex address
    if 3 - len(address)>0:
        address = "0"*(3 - len(address))+address
    op_code = MRI[strings[index1]][index2]

    assembled = op_code + address
    return hex(int(assembled,16))


def num_converter(word, number):
    #converts string number to hexadecimal 
    if word == PSEUDO[1]:  # word == HEX
        return hex(int(number))
    else:                            # word == DEC
        return hex(int(number))
