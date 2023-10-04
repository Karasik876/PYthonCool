name = str(input())
temp = ''
for i in name:
    if i != '.':
        temp+=i
    else:
        print(temp)
        temp = ''

if temp != '':
    print(temp)