import binascii

text_a = '1c0111001f010100061a024b53535009181c'
text_b = '686974207468652062756c6c277320657965'
target = '746865206b696420646f6e277420706c6179'

def fixed_xor(text_a, text_b):
    binary_a = binascii.unhexlify(text_a)
    binary_b = binascii.unhexlify(text_b)
    result = "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(binary_a, binary_b)])
    return binascii.hexlify(result)

if __name__ == '__main__':
    result = fixed_xor(text_a, text_b)
    print result
    print result == target
