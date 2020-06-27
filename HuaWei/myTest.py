def is_valid(key):
    if (key>='0'and key<='9') or (key>='a'and key<='z') or (key>='A' and key<='Z'):
        return True
    return False
if __name__ == "__main__":
    n = 100
    s =[]
    valid_str = []
    invalid_str = []
    bool_valid =True
    while n>0:
        a = input()
        if len(a) == 0:
            break
        if a[0] == ' ':
            break
        s.append(a)
        n -= 1
    if len(s) == 0:
        print("\n")
        print("\n")
    else:
        for word in s:
            bool_valid = True
            for j in range(len(word)):
                if not is_valid(word[j]):
                    invalid_str.append(word)
                    bool_valid = False
                    break
            if bool_valid:
                valid_str.append(word)
        dic = list(set(valid_str))
        dic.sort(key=valid_str.index)
        if len(dic) == 0:
            print('\n')
        else:
            print(' '.join(dic))
            e = ' '.join(dic)
        if len(invalid_str) == 0:
            print('\n')
        else:
            e = ' '.join(invalid_str)
            print(' '.join(invalid_str))
            e = ' '.join(invalid_str)