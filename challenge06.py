import binascii
import base64
from challenge4 import *
from operator import itemgetter

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

#print hamming_distance('this is a test', 'wokka wokka!!!')

# the keysize guessing part really doesn't matter that much
def guess_keysize(content, block_size=1, limit=4):
    hds = []
    for key_size in range(2, 41):
        hd = float(hamming_distance(content[0:key_size * block_size], content[key_size * block_size:key_size * block_size * 2])) / (key_size * block_size)
        hds.append((key_size, hd))

    hds = sorted(hds, key=itemgetter(1))
    return [pair[0] for pair in hds][:limit]

def transpose(content, key_size):
    result = [[] for _ in range(key_size)]
    for i, c in enumerate(content):
        result[i % key_size].append(c)

    return [''.join(char_list) for char_list in result]

def recover(content, transposed, key_size):
    result = ''
    n = len(content)
    for i in range(n):
        if transposed[i % key_size] == '':
            return ''
        result += transposed[i % key_size][i / key_size]
    return result

if __name__ == '__main__':
    content = base64.b64decode(open('06.txt', 'r').read())

    for KEYSIZE in range(2, 41):
        transposed = transpose(content, KEYSIZE)
        possible_plains = [item[1] for item in map(decrypt_single_xor, transposed)]
        decrypted = recover(content, possible_plains, KEYSIZE)
        if decrypted != '':
            print KEYSIZE
            print decrypted
