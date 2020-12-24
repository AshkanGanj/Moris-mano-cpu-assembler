from instruction_set import PSEUDO

def precompile(source):

    lines = source.split('\n')
    
    LC = 0
    symbols_address = dict()

    for line in lines:
        strings = line.split()
        if strings[0][-1] == ',':
            symbol = strings[0][:-1]
            symbols_address[symbol] = str(LC)
        elif strings[0] == PSEUDO[0]:
            LC = int(strings[1])
            continue
        elif strings[0] == PSEUDO[3]:
            break
        LC += 1

    return symbols_address