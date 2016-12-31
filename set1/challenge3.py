import binascii
from challenge2 import fixed_xor

cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def get_score(text):
    freq_dict = {
        'e': 12.02,
        't': 9.10,
        'a': 8.12,
        'o': 7.68,
        'i': 7.31,
        'n': 6.95,
        's': 6.28,
        'r': 6.02,
        'h': 5.92,
        'd': 4.32,
        'l': 3.98,
        'u': 2.88,
        'c': 2.71,
        'm': 2.61,
        'f': 2.30,
        'y': 2.11,
        'w': 2.09,
        'g': 2.03,
        'p': 1.82,
        'b': 1.49,
        'v': 1.11,
        'k': 0.69,
        'x': 0.17,
        'q': 0.11,
        'j': 0.10,
        'z': 0.07,
    }
    count_dict = {}
    total_count = 0
    for c in text:
        c = c.lower()
        if c <= 'z' and c >= 'a':
            total_count += 1
            count_dict[c] = count_dict.get(c, 0) + 1

    if float(total_count) / len(text) < 0.7:
        return 100

    score = 0
    for c in range(ord('a'), ord('z') + 1):
        c = chr(c)
        count_dict[c] = count_dict.get(c, 0) / float(total_count) * 100
        score += abs(count_dict[c] - freq_dict[c])

    return score

def single_char_xor(char, text):
    key = binascii.hexlify(char) * (len(text) / 2)
    return binascii.unhexlify(fixed_xor(text, key))

if __name__ == '__main__':
    score_dict = {}
    for k in range(ord('A'),ord('z')+1):
        k = chr(k)
        result = single_char_xor(k, cipher)
        score = get_score(result)
        score_dict[result] = score

    for text in sorted(score_dict, key=score_dict.get, reverse=True):
        print text, score_dict[text]
