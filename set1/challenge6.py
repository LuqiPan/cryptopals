import binascii
import base64
from challenge4 import *

def ascii2bin(text):
    return bin(int(binascii.hexlify(text), 16))[2:]

def hamming_distance(a, b):
    a_bin = ascii2bin(a)
    b_bin = ascii2bin(b)
    hd = 0
    for i, j in zip(a_bin, b_bin):
        if i != j:
            hd += 1

    return hd

if __name__ == '__main__':
    #line = open('6.txt', 'r').read().split('\n')
    content = base64.b64decode(open('6.txt', 'r').read())
    print content
    #for line in content:
        #print line
    #text = [base64.b64decode(line) for line in content]
    #for line in text:
        #print line

    normalized_distance = {}
    for KEYSIZE in range(2, 41):
        hd = hamming_distance(content[0:KEYSIZE], content[KEYSIZE:2 * KEYSIZE])
        normalized_distance[KEYSIZE] = float(hd) / KEYSIZE

    for KEYSIZE in range(2, 41):
        hd = hamming_distance(content[0:KEYSIZE*2], content[KEYSIZE*2:4*KEYSIZE])
        normalized_distance[KEYSIZE] = (normalized_distance[KEYSIZE] + float(hd) / KEYSIZE / 2) / 2

    for KEYSIZE in sorted(normalized_distance, key=normalized_distance.get)[0:3]:
        print normalized_distance[KEYSIZE], KEYSIZE
        BLOCKS = len(content) / KEYSIZE
        for i in range(0, KEYSIZE):
            block = ''
            for b in range(0, BLOCKS):
                block += content[b*KEYSIZE+i]
            result = decrypt_single_xor(binascii.hexlify(block), 1)
            for line in result:
                print line
