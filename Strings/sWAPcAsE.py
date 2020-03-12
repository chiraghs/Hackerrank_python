def swap_case(s):
    news=''
    for i in s:
        if i.isupper():
            news +=i.lower()
        else:
            news +=i.upper()    
    return news

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)    