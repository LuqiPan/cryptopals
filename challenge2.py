import binascii

text_a = binascii.unhexlify('1c0111001f010100061a024b53535009181c')
text_b = binascii.unhexlify('686974207468652062756c6c277320657965')
target = '746865206b696420646f6e277420706c6179'

def fixed_xor(text_a, text_b):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(text_a, text_b)])

if __name__ == '__main__':
    assert(fixed_xor(text_a, text_b) == binascii.unhexlify(target))
    print "PASS"
