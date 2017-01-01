import binascii
from challenge2 import fixed_xor

cipher_text = binascii.unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

def get_score(text):
    freq_dict = {
	' ': 18.28846265,
	'e': 10.26665037,
	't': 7.51699827,
	'a': 6.53216702,
	'o': 6.15957725,
	'n': 5.71201113,
	'i': 5.66844326,
	's': 5.31700534,
	'r': 4.98790855,
	'h': 4.97856396,
	'l': 3.31754796,
	'd': 3.28292310,
	'u': 2.27579536,
	'c': 2.23367596,
	'm': 2.02656783,
	'f': 1.98306716,
	'w': 1.70389377,
	'g': 1.62490441,
	'p': 1.50432428,
	'y': 1.42766662,
	'b': 1.25888074,
	'v': 0.79611644,
	'k': 0.56096272,
	'x': 0.14092016,
	'j': 0.09752181,
	'q': 0.08367550,
	'z': 0.05128469,
    }
    count_dict = {}
    total_count = 0
    for c in text:
        c = c.lower()
	if c in freq_dict:
            total_count += 1
            count_dict[c] = count_dict.get(c, 0) + 1

    if float(total_count) / len(text) < 0.7:
        return 200

    score = 0
    for c in range(ord('a'), ord('z') + 1):
        c = chr(c)
        count_dict[c] = count_dict.get(c, 0) / float(total_count) * 100
        score += abs(count_dict[c] - freq_dict[c])

    return score

def single_char_xor(char, text):
    key = char * len(text)
    return fixed_xor(key, text)

def decrypt_single_xor(cipher_text):
    lowest_score = 200
    plain_text = ''
    for k in range(0, 256):
        k = chr(k)
        decrypted_text = single_char_xor(k, cipher_text)
        score = get_score(decrypted_text)
        if score < lowest_score:
            plain_text = decrypted_text
            lowest_score = score

    return (lowest_score, plain_text)

if __name__ == '__main__':
    print decrypt_single_xor(cipher_text)[1]
    #print get_score('ETAOIN SHRDLU')
