class BadPKCS7PaddingException(Exception):
    pass

def is_valid_PKCS7_padding(text):
    padding_length = ord(text[-1])
    if padding_length > len(text):
        raise BadPKCS7PaddingException

    for i in range(padding_length):
        index = len(text) - 1 - i
        if text[index] != chr(padding_length):
            raise BadPKCS7PaddingException

    return True

if __name__ == '__main__':
    assert(is_valid_PKCS7_padding("ICE ICE BABY\x04\x04\x04\x04"))
    print 'PASS'

    try:
        is_valid_PKCS7_padding("ICE ICE BABY\x05\x05\x05\x05")
        print 'The program should never reach here'
    except BadPKCS7PaddingException:
        print 'PASS'

    try:
        is_valid_PKCS7_padding("ICE ICE BABY\x01\x02\x03\x04")
        print 'The program should never reach here'
    except BadPKCS7PaddingException:
        print 'PASS'
