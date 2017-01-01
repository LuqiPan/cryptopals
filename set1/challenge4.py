from challenge3 import *
from operator import itemgetter

if __name__ == '__main__':
    texts = open('4.txt', 'r').read().split('\n')

    candidates = []
    for text in texts:
        candidates.append(decrypt_single_xor(text))

    #print sorted(candidates, key=itemgetter(0))[:1][0][1]
    print sorted(candidates, key=itemgetter(0))[:1]
