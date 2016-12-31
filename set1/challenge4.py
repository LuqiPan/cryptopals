from challenge3 import *

if __name__ == '__main__':
    texts = open('4.txt', 'r').read().split('\n')

    score_dict = {}
    lowest_score = 99
    for text in texts:
        for k in range(0, 256):
            k = chr(k)
            decrypted_text = single_char_xor(k, text)
            score = get_score(decrypted_text)
            if score <= lowest_score:
                lowest_score = score
                print '----'
                print k
                print decrypted_text
                print score
                print '----'
