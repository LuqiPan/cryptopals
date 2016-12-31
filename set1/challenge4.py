from challenge3 import *
import ipdb
import simplejson

def decrypt_single_xor(text, candidate_number=1):
    score_dict = {}
    for k in range(0, 256):
        k = chr(k)
        new_text = single_char_xor(k, text)
        score_dict[new_text] = get_score(new_text)

    return sorted(score_dict, key=score_dict.get)[0:candidate_number]

if __name__ == '__main__':
    texts = open('4.txt', 'r').read().split('\n')

    score_dict = {}
    for text in texts:
        for k in range(0, 256):
            k = chr(k)
            new_text = single_char_xor(k, text)
            score_dict[new_text] = get_score(new_text)


    for text in sorted(score_dict, key=score_dict.get, reverse=True):
        if score_dict[text] < 80:
            print '----'
            print score_dict[text]
            print text
            print '----'
