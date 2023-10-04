v = str(input())

def doubles_check(s):
    check = '0000000000'
    for i in s:
        if i != ' ':
            if check[int(i)] == '0':
                check = check[:int(i)] + '1' + check[int(i)+1:]
            else:
                return False
    return True

print(doubles_check(v))


