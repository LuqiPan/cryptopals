def padding(text, length, char='\x04'):
    return text + (char * (length - len(text)))

if __name__ == '__main__':
    print padding('YELLOW SUBMARINE', 20)
