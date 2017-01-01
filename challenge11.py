import random
import os
from challenge10 import *
from challenge08 import is_encrypted_with_ECB

def generate_random_bytes(len=16):
    return os.urandom(len)

def encryption_oracle(input):
    rng = random.SystemRandom()

    prefix = generate_random_bytes(rng.randint(5, 10))
    suffix = generate_random_bytes(rng.randint(5, 10))
    key = generate_random_bytes()
    plain_text = prefix + input + suffix

    if rng.randint(0, 1) == 0:
        # ECB
        return (encrypt_AES_ECB(plain_text, key), 'ECB')
    else:
        # CBC
        return (encrypt_AES_CBC(plain_text, key, generate_random_bytes()), 'CBC')

if __name__ == '__main__':
    hit = 0
    total = 1024
    for i in range(total):
        cipher_text, mode = encryption_oracle(generate_random_bytes() * 3)
        #print '-----'
        guessed_mode = 'ECB' if is_encrypted_with_ECB(cipher_text) else 'CBC'
        #print mode
        #print guessed_mode
        #print guessed_mode == mode
        if guessed_mode == mode:
            hit += 1
        #print '-----'

    print "Accuracy:" + str(float(hit) / total)
