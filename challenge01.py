"""
https://cryptopals.com/sets/1/challenges/1
"""

import base64
import binascii


hex_text = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
base64_text = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'


def hex2base64(hex_text):
    return base64.b64encode(binascii.unhexlify(hex_text))

if __name__ == '__main__':
    assert(hex2base64(hex_text) == base64_text)
    print "PASS"
