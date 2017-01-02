import base64
import binascii
import ipdb
from challenge10 import *
from challenge08 import is_encrypted_with_ECB

KEY = binascii.unhexlify('17248db34138334ee0a0ae136858e486')
secret_text = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')

def oracle(input):
    plain_text = input + secret_text
    return encrypt_AES_ECB(plain_text, KEY)

def get_block_size():
    bp1 = None
    for i in range(0, 128):
        if i == 0:
            prev_length = len(oracle('a' * i))
        else:
            curr_length = len(oracle('a' * i))
            if curr_length != prev_length:
                prev_length = curr_length
                if not bp1:
                    bp1 = i
                else:
                    return i - bp1

def generate_dictionary(block_size, current_progress):
    dict = {}
    prefix = current_progress[-block_size+1:]
    for i in range(256):
        c = chr(i)
        input = prefix + c
        cipher_text = oracle(input)
        dict[cipher_text[:block_size]] = input
    return dict

def byte_at_a_time_ECB_decrypt(block_size, total_length=16):
    current_progress = '----------------'
    for index in range(total_length):
        block_index = index / 16
        index = index % 16
        dict = generate_dictionary(block_size, current_progress)
        prefix = current_progress[-block_size:-index-1]
        cipher_text = oracle(prefix)
        corresponding_cipher_block = cipher_text[block_size * block_index:block_size * (block_index + 1)]
        current_progress += dict[corresponding_cipher_block][-1]
    return current_progress

if __name__ == '__main__':
    print '> Stage 1- getting the block size:'
    block_size = get_block_size()
    print block_size
    print '> Stage 2- verifying the function it is using ECB mode...'
    print is_encrypted_with_ECB(oracle('A' * block_size * 2))
    print '> Stage 3- guessing the first block...'
    clear_text = byte_at_a_time_ECB_decrypt(block_size, len(secret_text))[block_size:]
    print clear_text
    print '> Stage 4- comparing with the actual secret...'
    print secret_text
    print secret_text == clear_text
    print '> FINISHED'
