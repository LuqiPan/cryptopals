import pprint

def is_encrypted_with_ECB(line):
    block_size = 16
    blocks = [line[i:i+block_size] for i in range(0, len(line), block_size)]
    if len(blocks) > len(set(blocks)):
        return True

if __name__ == '__main__':
    block_size = 16

    for line_number, line in enumerate(open('08.txt', 'r').readlines()):
        line = line.strip()
        if is_encrypted_with_ECB(line):
            print line_number
            print line
            #pprint.pprint([line[i:i+block_size] for i in range(0, len(line), block_size)])
            #pprint.pprint(set([line[i:i+block_size] for i in range(0, len(line), block_size)]))
