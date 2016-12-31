import base64
import binascii

text = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
target = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'


def hex2base64(text):
    binary = binascii.unhexlify(text)
    print binary
    return base64.b64encode(binary)

if __name__ == '__main__':
    result = hex2base64(text)
    print result
    print result == target
