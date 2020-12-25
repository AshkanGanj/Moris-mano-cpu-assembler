from instruction_set import PSEUDO

#make our symbols_address table
def precompile(lines):
    LC = 0
    symbols_address = dict()

    for line in lines:
        strings = line.split()
        if strings[0][-1] == ',':
            symbol = strings[0][:-1]
            symbols_address[symbol] = str(LC)
        #check if it is ORG 
        elif strings[0] == PSEUDO[0]:
            LC = int(strings[1])
            continue
        #check for END
        elif strings[0] == PSEUDO[3]:
            break
        LC += 1

    return symbols_address