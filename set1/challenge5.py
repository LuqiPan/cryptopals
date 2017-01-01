import binascii

def repeating_key_xor(key, text):
    result = ''
    for i, c in enumerate(text):
        result += chr(ord(key[i % len(key)]) ^ ord(c))
    return result

if __name__ == '__main__':
    line = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

    target = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

    result = binascii.hexlify(repeating_key_xor("ICE", line))
    print result == target
