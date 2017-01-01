def padding(text, length):
    len_diff = length - len(text)
    char = chr(len_diff)
    return text + (char * len_diff)

if __name__ == '__main__':
    assert(padding('YELLOW SUBMARINE', 20) == 'YELLOW SUBMARINE' + chr(4) * 4)
    assert(padding('YELLOW SUBMARINE', 32) == 'YELLOW SUBMARINE' + chr(16) * 16)
    print 'PASS'
