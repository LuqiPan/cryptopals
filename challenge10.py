from Crypto.Cipher import AES
from challenge2 import fixed_xor

KEY = 'YELLOW SUBMARINE'

def encrypt_AES_ECB(plain_text, KEY):
    cipher_suite = AES.new(KEY, AES.MODE_ECB)
    return cipher_suite.encrypt(plain_text)

def encrypt_AES_CBC_ref(plain_text, KEY, IV='\x00' * len(KEY)):
    cipher_suite = AES.new(KEY, AES.MODE_CBC, IV)
    return cipher_suite.encrypt(plain_text)

def encrypt_AES_CBC(plain_text, KEY, IV='\x00' * len(KEY)):
    cipher_text = ''
    block_size = len(KEY)
    previous_cipher_block = IV
    for i in range(0, len(plain_text), block_size):
        plain_block = plain_text[i:i+block_size]
        to_be_encrypted_block = fixed_xor(plain_block, previous_cipher_block)
        cipher_block = encrypt_AES_ECB(to_be_encrypted_block, KEY)
        cipher_text += cipher_block
        previous_cipher_block = cipher_block

    return cipher_text

def decrypt_AES_ECB(cipher_text, KEY):
    cipher_suite = AES.new(KEY, AES.MODE_ECB)
    return cipher_suite.decrypt(cipher_text)

def decrypt_AES_CBC(cipher_text, KEY, IV='\x00' * len(KEY)):
    clear_text = ''
    block_size = len(KEY)
    previous_cipher_block = IV
    for i in range(0, len(cipher_text), block_size):
        cipher_block = cipher_text[i:i+block_size]
        decrypted_text_block = decrypt_AES_ECB(cipher_block, KEY)
        clear_text_block = fixed_xor(decrypted_text_block, previous_cipher_block)
        clear_text += clear_text_block
        previous_cipher_block = cipher_block
    return clear_text

def decrypt_AES_CBC_ref(cipher_text, KEY, IV='\x00' * len(KEY)):
    cipher_suite = AES.new(KEY, AES.MODE_CBC, IV)
    return cipher_suite.decrypt(cipher_text)

if __name__ == '__main__':
    content = open('10.txt', 'r').read()
    plain_text = decrypt_AES_CBC(content, KEY)
    cipher_text = encrypt_AES_CBC(plain_text, KEY)
    assert(content == cipher_text)
    print 'PASS'
