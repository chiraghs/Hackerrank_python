def split_and_join(line):
    lista=line.split()
    newstr='-'.join(lista)
    return newstr

if __name__ == '__main__':
   line = input()
    result = split_and_join(line)
    print(result)    