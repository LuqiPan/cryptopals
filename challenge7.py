import base64
from Crypto.Cipher import AES

KEY = 'YELLOW SUBMARINE'

def decrypt_AES_ECB(cipher_text, KEY):
    decryption_suite = AES.new(KEY, AES.MODE_ECB)
    return decryption_suite.decrypt(cipher_text)


if __name__ == '__main__':
    cipher_text = base64.b64decode(open('7.txt', 'r').read())
    print decrypt_AES_ECB(cipher_text, KEY)
