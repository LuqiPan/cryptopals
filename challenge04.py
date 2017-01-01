from challenge3 import *
from operator import itemgetter

if __name__ == '__main__':
    texts = open('04.txt', 'r').read().split('\n')

    candidates = []
    for text in texts:
        text = binascii.unhexlify(text)
        candidates.append(decrypt_single_xor(text))

    print sorted(candidates, key=itemgetter(0))[0][1]
